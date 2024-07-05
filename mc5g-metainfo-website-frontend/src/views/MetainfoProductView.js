import {
  Box,
  PageContent,
} from 'grommet'
import {
  useEffect,
  useState,
} from 'react'
import { useParams } from 'react-router-dom'

import {
  ROLE_PRODUCT_RELEASE,
  getUserSelfRoles,
} from '../api/user'
import {
  computeRelatedSearch,
  renderState,
} from '../utils'

import ActionReleaseButton from '../components/ActionReleaseButton'
import ActionDownloadMetainfoButton from '../components/ActionDownloadMetainfoButton'
import MetainfoDeliverable from '../components/MetainfoDeliverable'
import MetainfoHeader from '../components/MetainfoHeader'
import MetainfoHistory from '../components/MetainfoHistory'
import MetainfoPackages from '../components/MetainfoPackages'
import MetainfoRelated from '../components/MetainfoRelated'
import MetainfoResultFor from '../components/MetainfoResultsFor'
import {
  generateLineStateFailed,
  generateLineStateReady,
  MetainfoStatus,
} from '../components/MetainfoStatus'
import ModalActionRelease from '../components/ModalActionRelease'
import TableArtifacts from '../components/TableArtifacts'

const statusLines = [
  {
    states: ["FT Ready", "IT Ready", "Val Ready", "QA Ready", "RC", "GA Released"],
    generator: generateLineStateReady,
  },
  {
    states: ["FT Ready", "IT Ready", "Val Ready", "QA Ready", "RC", "CA Released"],
    generator: generateLineStateReady,
  },
  {
    states: ["FT Failed", "IT Failed", "Val Failed", "QA Failed", "RC", "GA Released"],
    generator: generateLineStateFailed,
  }
]

const MetainfoProductView = ({ setExtraIcons, model, onParams = null, ...props }) => {
  const params = useParams()

  useEffect(() => {
    if (!onParams)
      return

    onParams(params)
  }, [onParams, params])

  const [showReleaseButton, setShowReleaseButton] = useState(false)
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

    setShowReleaseButton(
      (model.metainfo && model.metainfo.status === 'RC') &&
      (roles && roles.includes(ROLE_PRODUCT_RELEASE))
    )
  }, [model, roles])

  useEffect(() => {
    if (!model)
      return

    const newIcons = [
      <ActionDownloadMetainfoButton collection={model.collection} artifactId={model.artifactId} version={model.version} />
    ]

    if (showReleaseButton) {
      newIcons.push(
        <ActionReleaseButton onClick={
          () => setShowModal(
            <ModalActionRelease
              collection={model.collection}
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
  }, [setExtraIcons, model, showReleaseButton])

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
          <h1>Components</h1>
          {
            renderState(model.components, (components) => (
              <TableArtifacts collection='components' data={components.members} sortable={true} sort={{ property: 'ident.artifactId' }} nested={true} />
            ))
          }
          <h1>Test results</h1>
          {
            renderState(model.testResults, (testResults) => (
              <MetainfoResultFor metainfos={testResults.members} />
            ))
          }
          <h1>Deliverables</h1>
          <MetainfoDeliverable deliverable={metainfo.deliverable} />
          <h1>Packages</h1>
          <MetainfoPackages packages={metainfo.packages} metainfo={metainfo} />
          <h1>Component packages</h1>{
            renderState(model.componentsPackages, (packages) => (
              <MetainfoPackages packages={packages} metainfo={metainfo} sortable={true} sort={{ property: 'ident.artifactId' }} />
            ))
          }
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
          <h1>Solutions containing this product</h1>
          {
            renderState(model.relatedSolutions, (relatedSolutions) => (
              <MetainfoRelated collection='solutions' data={relatedSolutions}
                moreLink={computeRelatedSearch('solutions', model.artifactId, model.version, 'products')}
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

export default MetainfoProductView
