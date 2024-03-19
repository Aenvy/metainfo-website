import {
  Page,
} from 'grommet'
import {
  useEffect,
  useState,
} from 'react'
import { useParams } from 'react-router-dom'

import { MetainfoComponentModel } from '../models/MetainfoComponentModel'
import MetainfoComponentView from '../views/MetainfoComponentView'

const MetainfoComponentPage = ({ setExtraIcons, collection }) => {
  const { compGroupId, compArtifactId, compVersion } = useParams()

  const [dataModel, setDataModel] = useState(undefined)
  const [model,] = useState(() => new MetainfoComponentModel((newDataModel) => {
    setDataModel(newDataModel)
  }))

  useEffect(() => {
    model.load(collection, compGroupId, compArtifactId, compVersion)
  }, [collection, compGroupId, compArtifactId, compVersion, model])

  return (
    <Page>{
      dataModel ? <MetainfoComponentView setExtraIcons={setExtraIcons} model={dataModel} /> : null
    }</Page>
  )
}

export default MetainfoComponentPage
