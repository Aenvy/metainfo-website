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

import MetainfoTestView from '../views/MetainfoTestView'
import { MetainfoTestModel } from '../models/MetainfoTestModel'
import { MetainfoTreeDataProvider } from '../models/MetainfoTreeDataProvider'

const MetainfoTestPage = ({ setExtraIcons, collection }) => {
  const { groupId, artifactId, version } = useParams()

  const [dataProvider] = useState(new MetainfoTreeDataProvider())
  const [dataModel, setDataModel] = useState(undefined)
  const [model] = useState(() => new MetainfoTestModel((newDataModel) => {
    setDataModel(newDataModel)
  }, dataProvider))

  useEffect(() => {
    model.load(collection, groupId, artifactId, version)
  }, [collection, groupId, artifactId, version, model])

  return (
    <Page>
      <MetainfoTestView setExtraIcons={setExtraIcons} model={dataModel} />
    </Page>
  )
}

export default MetainfoTestPage
