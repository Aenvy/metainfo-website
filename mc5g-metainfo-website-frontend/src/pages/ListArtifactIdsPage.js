import {
  CheckBox,
  Page,
  PageContent,
  PageHeader,
} from 'grommet'
import {
  useEffect,
  useState,
} from 'react'
import { useSearchParams } from 'react-router-dom'

import TableArtifactsQueried from '../components/TableArtifactsQueried'

const AGGREGATE_ON = { 'latestFor': ['ident.groupId', 'ident.artifactId'] }
const COLUMNS_PRETTY = ['name', 'description']
const COLUMNS_RAW = ['ident.artifactId', 'ident.groupId']

function computeSearchParams(showDiscarded, showRawIdentifiers) {
  const value = {}

  if (showDiscarded) {
    value.showDiscarded = true
  }
  if (showRawIdentifiers) {
    value.showRawIdentifiers = true
  }

  return value
}

const ListArtifactIdsPage = ({ setExtraIcons, collection }) => {
  const [searchParams, setSearchParams] = useSearchParams()

  const [showDiscarded, setShowDiscarded] = useState(undefined)
  const [showRawIdentifiers, setShowRawIdentifiers] = useState(undefined)

  const [columns, setColumns] = useState(undefined)
  const [sort, setSort] = useState(undefined)

  function filter(item) {
    if (showDiscarded) {
      return true
    }

    return item.status !== 'Discarded'
  }

  useEffect(() => {
    setExtraIcons([])
  }, [setExtraIcons])

  useEffect(() => {
    const isShowDiscarded = searchParams.get('showDiscarded') === 'true'
    const isShowRawIdentifiers = searchParams.get('showRawIdentifiers') === 'true'

    setShowDiscarded(isShowDiscarded)
    setShowRawIdentifiers(isShowRawIdentifiers)

    var newColumns = [...isShowRawIdentifiers ? COLUMNS_RAW : COLUMNS_PRETTY]
    if (isShowDiscarded) {
      newColumns.push('discarded')
    }
    setColumns(newColumns)

    setSort(isShowRawIdentifiers ? {property: 'ident.artifactId'} : {property: 'name'})
  }, [searchParams])

  return (
    <Page>
      <PageContent>
        <PageHeader title={`${collection.charAt(0).toUpperCase() + collection.slice(1)}`} />
        <CheckBox
          label='Show discarded'
          value={showDiscarded}
          onClick={event => setSearchParams(computeSearchParams(event.target.checked, showRawIdentifiers))}
        />
        <CheckBox
          label='Show raw identifiers'
          value={showRawIdentifiers}
          onClick={event => setSearchParams(computeSearchParams(showDiscarded, event.target.checked))}
        />
        <TableArtifactsQueried
          collection={collection}
          aggregateOn={AGGREGATE_ON}
          columns={columns}
          sort={sort}
          displayIf={item => filter(item)}
        />
      </PageContent>
    </Page>
  )
}

export default ListArtifactIdsPage
