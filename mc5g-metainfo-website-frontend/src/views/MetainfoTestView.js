import {
  Box,
  PageContent,
} from 'grommet'
import {
  useEffect,
} from 'react'
import { useParams } from 'react-router-dom'

import { renderState } from '../utils'

import ActionDownloadMetainfoButton from '../components/ActionDownloadMetainfoButton'
import MetainfoHeader from '../components/MetainfoHeader'
import MetainfoHistory from '../components/MetainfoHistory'
import MetainfoPackages from '../components/MetainfoPackages'
import {
  generateLineStateFailed,
  generateLineStateReady,
  MetainfoStatus,
} from '../components/MetainfoStatus'

const statusLines = [
  {
    states: ["Init", "Passed"],
    generator: generateLineStateReady,
  },
  {
    states: ["Init", "Failed"],
    generator: generateLineStateFailed,
  },
]

const MetainfoTestView = ({ setExtraIcons, model, onParams = null, ...props }) => {
  const params = useParams()

  useEffect(() => {
    if (!onParams)
      return

    onParams(params)
  }, [onParams, params])

  useEffect(() => {
    if (!model)
      return

    const newIcons = [
      <ActionDownloadMetainfoButton collection={model.collection} groupId={model.groupId} artifactId={model.artifactId} version={model.version} />
    ]
    setExtraIcons(newIcons)
  }, [setExtraIcons, model])

  if (!model)
    return <PageContent {...props} />

  return (
    <PageContent {...props}>{
      renderState(model.metainfo, (metainfo) => (
        <Box>
          <MetainfoHeader collection={model.collection} metainfo={metainfo} />
          <MetainfoStatus status={metainfo.status} statusLines={statusLines} />
          <h1>Packages</h1>
          <MetainfoPackages packages={metainfo.packages} metainfo={metainfo} />
          <h1>History</h1>
          <MetainfoHistory history={metainfo.history} />
        </Box>
      ))
    }</PageContent>
  )
}

export default MetainfoTestView
