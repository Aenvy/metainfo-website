import {
  Box,
  PageContent,
} from 'grommet'
import {
  useEffect,
} from 'react'
import { useParams } from 'react-router-dom'

import {
  computeRelatedSearch,
  renderState,
} from '../utils'

import ActionDownloadMetainfoButton from '../components/ActionDownloadMetainfoButton'
import MetainfoHeader from '../components/MetainfoHeader'
import MetainfoHistory from '../components/MetainfoHistory'
import MetainfoPackages from '../components/MetainfoPackages'
import MetainfoRelated from '../components/MetainfoRelated'
import {
  generateLineStateFailed,
  generateLineStateReady,
  MetainfoStatus,
} from '../components/MetainfoStatus'
import TableArtifacts from '../components/TableArtifacts'

const statusLines = [
  {
    states: ["CT Ready", "FT Ready", "IT Ready", "Val Ready", "QA Ready", "RC", "GA Released"],
    generator: generateLineStateReady,
  },
  {
    states: ["CT Ready", "FT Ready", "IT Ready", "Val Ready", "QA Ready", "RC", "CA Released"],
    generator: generateLineStateReady,
  },
  {
    states: ["CT Failed", "FT Failed", "IT Failed", "Val Failed", "QA Failed", "RC", "GA Released"],
    generator: generateLineStateFailed,
  }
]

const MetainfoComponentView = ({ setExtraIcons, model, onParams = null, ...props }) => {
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
          <h1>Build dependencies</h1>
          {
            renderState(model.buildDependencies, (buildDependencies) => (
              <TableArtifacts collection='components' data={buildDependencies.members} sortable={true} sort={{ property: 'ident.artifactId' }} />
            ))
          }
          <h1>Runtime dependencies</h1>
          {
            renderState(model.runtimeDependencies, (runtimeDependencies) => (
              <TableArtifacts collection='components' data={runtimeDependencies.members} sortable={true} sort={{ property: 'ident.artifactId' }} />
            ))
          }
          <h1>Products containing this component</h1>
          {
            renderState(model.relatedProducts, (relatedProducts) => (
              <MetainfoRelated collection='products' data={relatedProducts}
                moreLink={computeRelatedSearch('products', model.groupId, model.artifactId, model.version, 'components')}
              />
            ))
          }
          <h1>History</h1>
          <MetainfoHistory history={metainfo.history} />
        </Box>
      ))
    }</PageContent>
  )
}

export default MetainfoComponentView
