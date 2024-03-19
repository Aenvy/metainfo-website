import {
  getArtifact,
  getArtifactListArtifacts,
  getListArtifacts,
} from '../api/metainfo'

import { MetainfoTreeDataProvider } from './MetainfoTreeDataProvider'

import { maxRelatedShown } from '../config'
import { computeRelatedFilters } from '../utils'

function computeResultsFilters(groupId, artifactId, version) {
  const versionRegex = `/${version.split('-').slice(0, 2).join('-').replaceAll('.', '\\.')}.*/`

  return { 'identifiers': { '$anyOf': [{ 'groupId': groupId, 'artifactId': artifactId, 'version': versionRegex }] } }
}

function mergeComponentPackages(metainfos) {
  var packages = {}
  for (const metainfo of metainfos) {
    for (const propertyName in metainfo.packages) {
      packages[propertyName] = [...packages[propertyName] || [], ...metainfo.packages[propertyName]]
    }
  }

  return packages
}

export class MetainfoProductModel {
  public onNewData: any
  public metainfoTreeDataProvider?: MetainfoTreeDataProvider

  public collection: string
  public groupId: string
  public artifactId: string
  public version: string

  public metainfo: any
  public components: any
  public componentsPackages: any
  public buildDependencies: any
  public runtimeDependencies: any
  public testResults: any
  public relatedSolutions: any

  constructor(onNewData: any, metainfoTreeDataProvider?: MetainfoTreeDataProvider) {
    this.onNewData = onNewData
    this.metainfoTreeDataProvider = metainfoTreeDataProvider
  }

  public load(collection: string, groupId: string, artifactId: string, version: string) {
    this.collection = collection
    this.groupId = groupId
    this.artifactId = artifactId
    this.version = version

    this.metainfo = undefined
    this.components = undefined
    this.componentsPackages = undefined
    this.buildDependencies = undefined
    this.runtimeDependencies = undefined
    this.testResults = undefined
    this.relatedSolutions = undefined

    this.notifyNewData()

    getArtifact(this.collection, this.groupId, this.artifactId, this.version)
      .then((result) => {
        if (!this.outdated(collection, groupId, artifactId, version)) {
          this.metainfo = result
          if (this.metainfoTreeDataProvider)
            this.metainfoTreeDataProvider.populateRootMetainfo(this.collection, result)

          this.notifyNewData()
        }
      }
      ).catch((error) => {
        if (!this.outdated(collection, groupId, artifactId, version)) {
          this.metainfo = error

          this.notifyNewData()
        }
      })

    getArtifactListArtifacts(this.collection, this.groupId, this.artifactId, this.version, 'components', 'full')
      .then((result) => {
        if (!this.outdated(collection, groupId, artifactId, version)) {
          this.components = result;
          this.componentsPackages = mergeComponentPackages(result.members)
          if (this.metainfoTreeDataProvider)
            this.metainfoTreeDataProvider.populateMetainfos('components', result.members)

          this.notifyNewData()
        }
      }
      ).catch((error) => {
        if (!this.outdated(collection, groupId, artifactId, version)) {
          this.components = error;
          this.componentsPackages = error;

          this.notifyNewData()
        }
      })

    getArtifactListArtifacts(this.collection, this.groupId, this.artifactId, this.version, 'components/buildDependencies', 'summary')
      .then((result) => {
        if (!this.outdated(collection, groupId, artifactId, version)) {
          this.buildDependencies = result;
          this.notifyNewData()
        }
      }
      ).catch((error) => {
        if (!this.outdated(collection, groupId, artifactId, version)) {
          this.buildDependencies = error;

          this.notifyNewData()
        }
      })

    getArtifactListArtifacts(this.collection, this.groupId, this.artifactId, this.version, 'components/runtimeDependencies', 'summary')
      .then((result) => {
        if (!this.outdated(collection, groupId, artifactId, version)) {
          this.runtimeDependencies = result;

          this.notifyNewData()
        }
      }
      ).catch((error) => {
        if (!this.outdated(collection, groupId, artifactId, version)) {
          this.runtimeDependencies = error;

          this.notifyNewData()
        }
      })

      getListArtifacts('results', 'full', computeResultsFilters(this.groupId, this.artifactId, this.version), { 'earliestFor': ['ident.groupId', 'ident.artifactId', 'testType']})
      .then((result) => {
        if (!this.outdated(collection, groupId, artifactId, version)) {
          this.testResults = result;

          this.notifyNewData()
        }
      }
      ).catch((error) => {
        if (!this.outdated(collection, groupId, artifactId, version)) {
          this.testResults = error;

          this.notifyNewData()
        }
      })

      getListArtifacts('solutions', 'summary', computeRelatedFilters(this.groupId, this.artifactId, this.version, 'products'), null, 0, maxRelatedShown)
        .then((result) => {
          if (!this.outdated(collection, groupId, artifactId, version)) {
            this.relatedSolutions = result;
  
            this.notifyNewData()
          }
        }
        ).catch((error) => {
          if (!this.outdated(collection, groupId, artifactId, version)) {
            this.relatedSolutions = error;
  
            this.notifyNewData()
          }
        })
  }

  public outdated(collection: string, groupId: string, artifactId: string, version: string): boolean {
    return this.collection !== collection ||
      this.groupId !== groupId ||
      this.artifactId !== artifactId ||
      this.version !== version
  }

  public getDataModel() {
    return {
      collection: this.collection,
      groupId: this.groupId,
      artifactId: this.artifactId,
      version: this.version,
      metainfo: this.metainfo,
      components: this.components,
      componentsPackages: this.componentsPackages,
      buildDependencies: this.buildDependencies,
      runtimeDependencies: this.runtimeDependencies,
      testResults: this.testResults,
      relatedSolutions: this.relatedSolutions,
    }
  }

  public notifyNewData() {
    this.onNewData(this.getDataModel())
  }
}
