import {
  Box,
  PageContent,
  Button
} from 'grommet'
import {
  Archive
} from 'grommet-icons'
import {
  useEffect,
  useState,
} from 'react'
import { useParams } from 'react-router-dom'

import {
  ROLE_SOLUTION_BRANCH,
  getUserSelfRoles,
} from '../api/user'
import { renderState } from '../utils'

import ActionBranchButton from '../components/ActionBranchButton'
import ActionDownloadMetainfoButton from '../components/ActionDownloadMetainfoButton'
import MetainfoTestCampaigns from '../components/MetainfoTestCampaigns'
import MetainfoHeader from '../components/MetainfoHeader'
import MetainfoHistory from '../components/MetainfoHistory'
import {
  generateLineStateFailed,
  generateLineStateReady,
  MetainfoStatus,
} from '../components/MetainfoStatus'
import ModalActionBranch from '../components/ModalActionBranch'
import TableArtifacts from '../components/TableArtifacts'

const statusLines = [
  {
    states: ["Val Ready", "QA Ready", "RC", "GA Released"],
    generator: generateLineStateReady,
  },
  {
    states: ["Val Ready", "QA Ready", "RC", "CA Released"],
    generator: generateLineStateReady,
  },
  {
    states: ["Val Ready", "QA Failed", "RC", "GA Released"],
    generator: generateLineStateFailed,
  }
]

const MetainfoSolutionView = ({ setExtraIcons, model, onParams = null, ...props }) => {
  const params = useParams()

  useEffect(() => {
    if (!onParams)
      return

    onParams(params)
  }, [onParams, params])

  const [showBranchButton, setShowBranchButton] = useState(false)
  const [showModal, setShowModal] = useState(null)
  const [roles, setRoles] = useState([])

  useEffect(() => {
    getUserSelfRoles().then(
      result => { setRoles(result) }
    ).catch((error) => {
      setRoles(error)
    })
  }, [])

  useEffect(() => {
    if (!model)
      return

    setShowBranchButton(
      (model.metainfo && model.metainfo.status === 'QA Ready') &&
      (roles && roles.includes(ROLE_SOLUTION_BRANCH))
    )
  }, [model, roles])

  useEffect(() => {
    const newIcons = [
      <ActionDownloadMetainfoButton collection={model.collection} groupId={model.groupId} artifactId={model.artifactId} version={model.version} />
    ]

    if (showBranchButton) {
      newIcons.push(
        <ActionBranchButton onClick={
          event => setShowModal(
            <ModalActionBranch
              collection={model.collection}
              groupId={model.groupId}
              artifactId={model.artifactId}
              version={model.version}
              onDismiss={() => setShowModal(null)}
            />
          )
        }
        />
      )
    }

    setExtraIcons(newIcons)
  }, [setExtraIcons, model, showBranchButton])

  if (!model)
    return <PageContent {...props} />

  return (
    <PageContent {...props}>{
      renderState(model.metainfo, (metainfo) => (
        <Box>
          {
            showModal ? showModal : null
          }
          <MetainfoHeader collection={model.collection} metainfo={metainfo} />
          <MetainfoStatus status={metainfo.status} statusLines={statusLines} />
          <h1>Products</h1>
          {
            renderState(model.products, (metainfos) => (
              <TableArtifacts collection='products' data={metainfos.members} sortable={true} sort={{ property: 'ident.artifactId' }} nested={true} />
            ))
          }
          <h1>Test campaigns</h1>
          <MetainfoTestCampaigns testCampaigns={metainfo.testCampaigns} />
          <h1>Components</h1>
          {
            renderState(model.components, (metainfos) => (
              <TableArtifacts collection='components' data={metainfos.members} sortable={true} sort={{ property: 'ident.artifactId' }} />
            ))
          }
          <h1>Build dependencies</h1>
          {
            renderState(model.buildDependencies, (metainfos) => (
              <TableArtifacts collection='components' data={metainfos.members} sortable={true} sort={{ property: 'ident.artifactId' }} />
            ))
          }
          <h1>Runtime dependencies</h1>
          {
            renderState(model.runtimeDependencies, (metainfos) => (
              <TableArtifacts collection='components' data={metainfos.members} sortable={true} sort={{ property: 'ident.artifactId' }} />
            ))
          }
          <h1>History</h1>
          <MetainfoHistory history={metainfo.history} />
        </Box>
      ))
    }</PageContent>
  )
}

export default MetainfoSolutionView
