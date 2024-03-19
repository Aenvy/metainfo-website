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
  useParams,
} from 'react-router-dom'

import {
  renderState,
} from '../utils'

import MetainfoComponentView from '../views/MetainfoComponentView'
import MetainfoProductView from '../views/MetainfoProductView'
import NotFoundView from '../views/NotFoundView'
import { SidebarMetainfoTree } from '../components/SidebarMetainfoTree'
import { MetainfoComponentModel } from '../models/MetainfoComponentModel'
import { MetainfoProductModel } from '../models/MetainfoProductModel'
import { MetainfoTreeDataProvider } from '../models/MetainfoTreeDataProvider'

const MetainfoProductPage = ({ setExtraIcons, collection }) => {
  const { prodGroupId, prodArtifactId, prodVersion } = useParams()

  const [dataProvider] = useState(new MetainfoTreeDataProvider())
  const [dataModel, setDataModel] = useState(undefined)
  const [model] = useState(() => new MetainfoProductModel((newDataModel) => {
    setDataModel(newDataModel)
  }, dataProvider))

  const [componentIdent, setComponentIdent] = useState(undefined)
  const [componentDataModel, setComponentDataModel] = useState(undefined)
  const [componentModel] = useState(() => new MetainfoComponentModel((newDataModel) => {
    setComponentDataModel(newDataModel)
  }))

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
    model.load(collection, prodGroupId, prodArtifactId, prodVersion)
  }, [collection, prodGroupId, prodArtifactId, prodVersion, model])

  useEffect(() => {
    componentIdent && componentModel.load(componentIdent.collection, componentIdent.groupId, componentIdent.artifactId, componentIdent.version)
  }, [componentIdent, componentModel])

  return renderState(model.metainfo, (metainfo) => (
    <Page>
      <Grid columns={['medium', 'flex']}>
        <SidebarMetainfoTree collection={collection} metainfo={metainfo} dataProvider={dataProvider} />
        <Routes>
          <Route index element={
            <MetainfoProductView setExtraIcons={setExtraIcons} model={dataModel} alignSelf='top' />
          } />
          <Route path='components/:compGroupId/:compArtifactId/:compVersion' element={
            <MetainfoComponentView setExtraIcons={setExtraIcons} model={componentDataModel} alignSelf='top'
              onParams={updateComponentIdent}
            />
          } />
          <Route path='*' element={<NotFoundView setExtraIcons={setExtraIcons} alignSelf='top' />} />
        </Routes>
      </Grid>
    </Page>
  ))
}

export default MetainfoProductPage
