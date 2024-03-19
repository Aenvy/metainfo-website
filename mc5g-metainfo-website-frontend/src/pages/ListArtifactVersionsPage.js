import {
  Page,
  PageContent,
  PageHeader,
} from 'grommet'
import {
  useEffect,
} from 'react'
import {
  useParams,
  useSearchParams,
} from 'react-router-dom'

import {
  columnsPerCollection,
  statusesForCollection,
} from '../api/metainfo'

import {
  displayIfStatusFilter,
  groupByToAggregateOn,
  statusesFromSearchParams,
  statusesToSearchParams,
} from '../utils'

import SearchMetainfoLatestBy from '../components/SearchMetainfoLatestBy'
import SearchMetainfoStatus from '../components/SearchMetainfoStatus'
import TableArtifactsQueried from '../components/TableArtifactsQueried'

const ListArtifactVersionsPage = ({ setExtraIcons, collection }) => {
  const allStatuses = statusesForCollection(collection)
  const hiddenColumns = [
    'ident.groupId',
    'ident.artifactId',
  ]

  const [searchParams, setSearchParams] = useSearchParams()
  const { groupId, artifactId } = useParams()

  const filters = {
    'ident': {
      'groupId': groupId,
      'artifactId': artifactId,
    },
  }

  function getStatuses() {
    return statusesFromSearchParams(searchParams.get('status'))
  }

  function setStatuses(value) {
    searchParams.set('status', statusesToSearchParams(value))
    setSearchParams(searchParams)
  }

  function getGroupBy() {
    return (searchParams.get('groupBy') || 'date')
  }

  function setGroupBy(value) {
    searchParams.set('groupBy', value)
    setSearchParams(searchParams)
  }

  useEffect(() => {
    setExtraIcons([])
  }, [setExtraIcons])

  return (
    <Page>
      <PageContent>
        <PageHeader title={`${collection.charAt(0).toUpperCase() + collection.slice(1, -1)} ${artifactId} versions`} />
        <SearchMetainfoStatus collection={collection} allStatuses={allStatuses} activeStatuses={getStatuses()} onChange={event => setStatuses(event.value)} />
        <SearchMetainfoLatestBy collection={collection} value={getGroupBy()} onChange={event => setGroupBy(event.target.value)} />
        <TableArtifactsQueried
          collection={collection}
          filters={filters}
          aggregateOn={groupByToAggregateOn[getGroupBy()]}
          columns={columnsPerCollection(collection).filter(column => !hiddenColumns.includes(column))}
          displayIf={displayIfStatusFilter(getStatuses())}
        />
      </PageContent>
    </Page>
  )
}

export default ListArtifactVersionsPage
