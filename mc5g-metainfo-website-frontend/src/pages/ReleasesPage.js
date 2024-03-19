import {
  Grid,
  Page,
} from 'grommet'
import {
  useEffect,
  useState,
} from 'react'
import {
  Route,
  Routes,
  useLocation,
} from 'react-router-dom'

import {
  getListArtifacts,
} from '../api/metainfo'

import LatestReleasesView from '../views/LatestReleasesView'
import MetainfoComponentView from '../views/MetainfoComponentView'
import MetainfoProductView from '../views/MetainfoProductView'
import NotFoundView from '../views/NotFoundView'
import { SidebarReleaseTree } from '../components/SidebarMetainfoTree'
import { MetainfoComponentModel } from '../models/MetainfoComponentModel'
import { MetainfoProductModel } from '../models/MetainfoProductModel'
import { MetainfoTreeDataProvider } from '../models/MetainfoTreeDataProvider'

const FILTERS = { "tags": { "$allOf": ["/[0-9]\\.[0-9]{4}\\.[0-9]+(-RC[0-9]+)?$/"] }, "status": "/RC|CA Released|GA Released/" }
const AGGREGATE_ON = { 'earliestFor': ['ident.groupId', 'ident.artifactId', 'ident.version:date'] }

const TAG_RELEASE_REGEX = /([0-9]\.[0-9]{4}\.[0-9]+(-RC[0-9]+)?)$/

function tagToRelease(tag) {
  const result = tag.match(TAG_RELEASE_REGEX)
  return result ? result[0] : null
}

function versionsToReleases(versions) {
  if (versions === undefined) {
    return undefined
  }

  var releases = new Map()
  for (let version of versions.members) {
    for (let tag of version.tags) {
      const release = tagToRelease(tag)

      if (release) {
        releases.set(release, {
          'release': release,
          products: []
        })
      }
    }
  }

  for (let version of versions.members) {
    for (let tag of version.tags) {
      const release = tagToRelease(tag)

      if (release) {
        releases.get(release).products.push(version)
      }
    }
  }

  var values = [...releases.values()]
  values.sort((a, b) => {
    const aValue = a.release.split(/[^0-9]+/).map(x => parseInt(x))
    const bValue = b.release.split(/[^0-9]+/).map(x => parseInt(x))
    for (var index = 0; index < Math.min(aValue.length, bValue.length); index++) {
      if (aValue[index] !== bValue[index]) {
        return aValue[index] - bValue[index]
      }
    }
    return bValue.length - aValue.length
  })
  values.reverse()
  return values
}

const ReleasesPage = ({ setExtraIcons }) => {
  const { hash, key } = useLocation()

  const [versions, setVersions] = useState(undefined)
  const [releases, setReleases] = useState(undefined)

  const [dataProvider] = useState(new MetainfoTreeDataProvider('/'))

  useEffect(() => {
    getListArtifacts('products', 'summary', FILTERS, AGGREGATE_ON).then(
      result => setVersions(result)
    ).catch((error) => {
      setVersions(error)
    })
  }, [])

  useEffect(() => {
    if (versions !== undefined) {
      dataProvider.populateMetainfos('products', versions.members)
    }

    setReleases(versionsToReleases(versions))
  }, [dataProvider, versions])

  useEffect(() => {
    if (releases !== undefined) {
      dataProvider.populateTreeItems(releases.map(release => {
        const children = release.products.map(product => `products#${product.ident.groupId}#${product.ident.artifactId}#${product.ident.version}`)

        return {
          index: `releases#${release.release}`,
          data: `${release.release}`,
          isFolder: true,
          children: children,
          canMove: false,
          canRename: false,
        }
      }))

      dataProvider.populateTreeItem({
        index: `root`,
        data: `Releases`,
        isFolder: true,
        children: releases.map(release => `releases#${release.release}`),
        canMove: false,
        canRename: false,
      })
    }
  }, [dataProvider, releases])

  useEffect(() => {
    if (hash) {
      const targetElement = document.getElementById(hash.substring(1))
      targetElement?.scrollIntoView({ behavior: 'smooth' })
    }
  }, [key, hash])

  const [productIdent, setProductIdent] = useState(undefined)
  const [productDataModel, setProductDataModel] = useState(undefined)
  const [productModel] = useState(() => new MetainfoProductModel((newDataModel) => {
    setProductDataModel(newDataModel)
  }))

  const [componentIdent, setComponentIdent] = useState(undefined)
  const [componentDataModel, setComponentDataModel] = useState(undefined)
  const [componentModel] = useState(() => new MetainfoComponentModel((newDataModel) => {
    setComponentDataModel(newDataModel)
  }))

  const updateProductIdent = (params) => {
    const newProductIdent = {
      collection: 'products',
      groupId: params.prodGroupId,
      artifactId: params.prodArtifactId,
      version: params.prodVersion,
    }

    if (!productIdent ||
      productIdent.collection !== newProductIdent.collection ||
      productIdent.groupId !== newProductIdent.groupId ||
      productIdent.artifactId !== newProductIdent.artifactId ||
      productIdent.version !== newProductIdent.version
    ) {
      setProductIdent(newProductIdent)
    }
  }

  const updateComponentIdent = (params) => {
    const newComponentIdent = {
      collection: 'components',
      groupId: params.compGroupId,
      artifactId: params.compArtifactId,
      version: params.compVersion,
    }

    if (!componentIdent ||
      componentIdent.collection !== newComponentIdent.collection ||
      componentIdent.groupId !== newComponentIdent.groupId ||
      componentIdent.artifactId !== newComponentIdent.artifactId ||
      componentIdent.version !== newComponentIdent.version
    ) {
      setComponentIdent(newComponentIdent)
    }
  }

  useEffect(() => {
    productIdent && productModel.load(productIdent.collection, productIdent.groupId, productIdent.artifactId, productIdent.version)
  }, [productIdent, productModel])

  useEffect(() => {
    componentIdent && componentModel.load(componentIdent.collection, componentIdent.groupId, componentIdent.artifactId, componentIdent.version)
  }, [componentIdent, componentModel])

  return (
    <Page>
      <Grid columns={['medium', 'flex']}>
        <SidebarReleaseTree dataProvider={dataProvider} />
        <Routes>
          <Route index element={
            <LatestReleasesView setExtraIcons={setExtraIcons} releases={releases} nested={true} />
          } />
          <Route path=':release/products/:prodGroupId/:prodArtifactId/:prodVersion' element={
            <MetainfoProductView setExtraIcons={setExtraIcons} model={productDataModel}
              onParams={updateProductIdent} alignSelf='top'
            />
          } />
          <Route path=':release/products/:prodGroupId/:prodArtifactId/:prodVersion/components/:compGroupId/:compArtifactId/:compVersion' element={
            <MetainfoComponentView setExtraIcons={setExtraIcons} model={componentDataModel}
              onParams={updateComponentIdent} alignSelf='top'
            />
          } />
          <Route path='*' element={<NotFoundView setExtraIcons={setExtraIcons} alignSelf='top' />} />
        </Routes>
      </Grid>
    </Page>
  )
}

export default ReleasesPage
