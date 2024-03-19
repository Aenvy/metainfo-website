import {
  Box,
  Text,
  PageContent,
} from 'grommet'
import {
  useEffect,
} from 'react'
import {
  Link,
  useParams,
} from 'react-router-dom'

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
import MetainfoResultTestSuites from '../components/MetainfoResultTestSuites'
import TableArtifacts from '../components/TableArtifacts'

const statusLines = [
  {
    states: ["Passed"],
    generator: generateLineStateReady,
  },
  {
    states: ["Failed"],
    generator: generateLineStateFailed,
  },
]

const MetainfoResultView = ({ setExtraIcons, model, onParams = null, ...props }) => {
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
          <h1>Results summary</h1>
          {
            metainfo.deployer
              ? <Text>Deployer version: <Link to={`/products/${metainfo.deployer.groupId}/${metainfo.deployer.artifactId}/${metainfo.deployer.version}`}>{metainfo.deployer.version}</Link></Text>
              : null
          }
          {
            metainfo.test
              ? <Text>Test version: <Link to={`/tests/${metainfo.test.groupId}/${metainfo.test.artifactId}/${metainfo.test.version}`}>{metainfo.test.version}</Link></Text>
              : null
          }
          {
            metainfo.tool
              ? <Text>Tool version: {metainfo.tool.name} {metainfo.tool.version}</Text>
              : null
          }
          {
            metainfo.testSuites
              ? <MetainfoResultTestSuites data={Object.values(metainfo.testSuites)} />
              : null
          }
          <h1>Products tested</h1>
          {
            renderState(model.productsTested, (productsTested) => (
              <TableArtifacts collection='products' data={productsTested.members} />
            ))
          }
          <h1>Packages</h1>
          <MetainfoPackages packages={metainfo.packages} metainfo={metainfo} />
          <h1>History</h1>
          <MetainfoHistory history={metainfo.history} />
        </Box>
      ))
    }</PageContent>
  )
}

export default MetainfoResultView
