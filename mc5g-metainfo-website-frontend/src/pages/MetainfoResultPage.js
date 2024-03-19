import {
  Page,
} from 'grommet'
import {
  useEffect,
  useState,
} from 'react'
import {
  useParams,
} from 'react-router-dom'

import MetainfoResultView from '../views/MetainfoResultView'
import { MetainfoResultModel } from '../models/MetainfoResultModel'
import { MetainfoTreeDataProvider } from '../models/MetainfoTreeDataProvider'

const MetainfoResultPage = ({ setExtraIcons, collection }) => {
  const { groupId, artifactId, version } = useParams()

  const [dataProvider] = useState(new MetainfoTreeDataProvider())
  const [dataModel, setDataModel] = useState(undefined)
  const [model] = useState(() => new MetainfoResultModel((newDataModel) => {
    setDataModel(newDataModel)
  }, dataProvider))

  useEffect(() => {
    model.load(collection, groupId, artifactId, version)
  }, [collection, groupId, artifactId, version, model])

  return (
    <Page>
      <MetainfoResultView setExtraIcons={setExtraIcons} model={dataModel} />
    </Page>
  )
}

export default MetainfoResultPage
