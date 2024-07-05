import {
  getArtifact,
  getArtifactListArtifacts,
  getListArtifacts,
} from '../api/metainfo'

import { MetainfoTreeDataProvider } from './MetainfoTreeDataProvider'

import { maxRelatedShown } from '../config'
import { computeRelatedFilters } from '../utils'

export class MetainfoComponentModel {
  public onNewData: any
  public metainfoTreeDataProvider?: MetainfoTreeDataProvider

  public collection: string
  public artifactId: string
  public version: string

  public metainfo: any
  public buildDependencies: any
  public runtimeDependencies: any
  public relatedProducts: any

  constructor(onNewData: any, metainfoTreeDataProvider?: MetainfoTreeDataProvider) {
    this.onNewData = onNewData
    this.metainfoTreeDataProvider = metainfoTreeDataProvider
  }

  public load(collection: string, artifactId: string, version: string) {
    this.collection = collection
    this.artifactId = artifactId
    this.version = version

    this.metainfo = undefined
    this.buildDependencies = undefined
    this.runtimeDependencies = undefined
    this.relatedProducts = undefined

    this.notifyNewData()

    getArtifact(this.collection, this.artifactId, this.version)
      .then((result) => {
        if (!this.outdated(collection, artifactId, version)) {
          this.metainfo = result

          this.notifyNewData()
        }
      }
      ).catch((error) => {
        if (!this.outdated(collection, artifactId, version)) {
          this.metainfo = error

          this.notifyNewData()
        }
      })

    getArtifactListArtifacts(this.collection, this.artifactId, this.version, 'buildDependencies', 'summary')
      .then((result) => {
        if (!this.outdated(collection, artifactId, version)) {
          this.buildDependencies = result;

          this.notifyNewData()
        }
      }
      ).catch((error) => {
        if (!this.outdated(collection, artifactId, version)) {
          this.buildDependencies = error;

          this.notifyNewData()
        }
      })

    getArtifactListArtifacts(this.collection, this.artifactId, this.version, 'runtimeDependencies', 'summary')
      .then((result) => {
        if (!this.outdated(collection, artifactId, version)) {
          this.runtimeDependencies = result;

          this.notifyNewData()
        }
      }
      ).catch((error) => {
        if (!this.outdated(collection, artifactId, version)) {
          this.runtimeDependencies = error;

          this.notifyNewData()
        }
      })

    getListArtifacts('products', 'summary', computeRelatedFilters(this.artifactId, this.version, 'components'), null, 0, maxRelatedShown)
      .then((result) => {
        if (!this.outdated(collection, artifactId, version)) {
          this.relatedProducts = result;

          this.notifyNewData()
        }
      }
      ).catch((error) => {
        if (!this.outdated(collection, artifactId, version)) {
          this.relatedProducts = error;

          this.notifyNewData()
        }
      })
  }

  public outdated(collection: string, artifactId: string, version: string): boolean {
    return this.collection !== collection ||
      this.artifactId !== artifactId ||
      this.version !== version
  }

  public getDataModel() {
    return {
      collection: this.collection,
      artifactId: this.artifactId,
      version: this.version,
      metainfo: this.metainfo,
      buildDependencies: this.buildDependencies,
      runtimeDependencies: this.runtimeDependencies,
      relatedProducts: this.relatedProducts,
    }
  }

  public notifyNewData() {
    this.onNewData(this.getDataModel())
  }
}
