import { getArtifact } from '../api/metainfo'

import { MetainfoTreeDataProvider } from './MetainfoTreeDataProvider'

export class MetainfoTestModel {
  public onNewData: any
  public metainfoTreeDataProvider?: MetainfoTreeDataProvider

  public collection: string
  public artifactId: string
  public version: string

  public metainfo: any

  constructor(onNewData: any, metainfoTreeDataProvider?: MetainfoTreeDataProvider) {
    this.onNewData = onNewData
    this.metainfoTreeDataProvider = metainfoTreeDataProvider
  }

  public load(collection: string, artifactId: string, version: string) {
    this.collection = collection
    this.artifactId = artifactId
    this.version = version

    this.metainfo = undefined

    this.notifyNewData()

    getArtifact(this.collection, this.artifactId, this.version)
      .then((result) => {
        if (!this.outdated(collection, artifactId, version)) {
          this.metainfo = result
          if (this.metainfoTreeDataProvider)
            this.metainfoTreeDataProvider.populateRootMetainfo(this.collection, result)

          this.notifyNewData()
        }
      }
      ).catch((error) => {
        if (!this.outdated(collection, artifactId, version)) {
          this.metainfo = error

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
    }
  }

  public notifyNewData() {
    this.onNewData(this.getDataModel())
  }
}
