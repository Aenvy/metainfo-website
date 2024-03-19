import {
  getArtifact,
  getArtifactListArtifacts,
} from '../api/metainfo'

import { MetainfoTreeDataProvider } from './MetainfoTreeDataProvider'

export class MetainfoSolutionModel {
  public onNewData: any
  public metainfoTreeDataProvider?: MetainfoTreeDataProvider

  public collection: string
  public groupId: string
  public artifactId: string
  public version: string

  public metainfo: any
  public products: any
  public components: any
  public buildDependencies: any
  public runtimeDependencies: any

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
    this.products = undefined
    this.components = undefined
    this.buildDependencies = undefined
    this.runtimeDependencies = undefined

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

    getArtifactListArtifacts(this.collection, this.groupId, this.artifactId, this.version, 'products', 'summary')
      .then((result) => {
        if (!this.outdated(collection, groupId, artifactId, version)) {
          this.products = result;

          if (this.metainfoTreeDataProvider)
            this.metainfoTreeDataProvider.populateMetainfos('products', result.members)

          this.notifyNewData()
        }
      }
      ).catch((error) => {
        if (!this.outdated(collection, groupId, artifactId, version)) {
          this.products = error;

          this.notifyNewData()
        }
      })

    getArtifactListArtifacts(this.collection, this.groupId, this.artifactId, this.version, 'products/components', 'summary')
      .then((result) => {
        if (!this.outdated(collection, groupId, artifactId, version)) {
          this.components = result;

          if (this.metainfoTreeDataProvider)
            this.metainfoTreeDataProvider.populateMetainfos('components', result.members)

          this.notifyNewData()
        }
      }
      ).catch((error) => {
        if (!this.outdated(collection, groupId, artifactId, version)) {
          this.components = error;

          this.notifyNewData()
        }
      })

    getArtifactListArtifacts(this.collection, this.groupId, this.artifactId, this.version, 'products/components/buildDependencies', 'summary')
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

    getArtifactListArtifacts(this.collection, this.groupId, this.artifactId, this.version, 'products/components/runtimeDependencies', 'summary')
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
      products: this.products,
      components: this.components,
      buildDependencies: this.buildDependencies,
      runtimeDependencies: this.runtimeDependencies,
    }
  }

  public notifyNewData() {
    this.onNewData(this.getDataModel())
  }
}
