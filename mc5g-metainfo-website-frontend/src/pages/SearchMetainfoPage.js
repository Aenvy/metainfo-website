import {
  Box,
  Button,
  FormField,
  Page,
  PageContent,
  PageHeader,
  Select,
  Spinner,
  Text,
} from 'grommet'
import { Download } from 'grommet-icons'
import {
  useEffect,
  useState,
} from 'react'
import { useSearchParams } from 'react-router-dom'

import {
  columnsPerCollection,
  downloadListArtifactsCsv,
  statusesForCollection,
} from '../api/metainfo'

import {
  renderState,
  displayIfStatusFilter,
  groupByToAggregateOn,
  statusesFromSearchParams,
  statusesToSearchParams,
} from '../utils'

import {
  ROLE_PRODUCT_RELEASE,
  getUserSelf,
  getUserSelfRoles,
} from '../api/user'

import SearchMetainfoFilters from '../components/SearchMetainfoFilters'
import SearchMetainfoLatestBy from '../components/SearchMetainfoLatestBy'
import SearchMetainfoStatus from '../components/SearchMetainfoStatus'
import TableArtifactsQueried from '../components/TableArtifactsQueried'

const validMetainfoTypes = [
  'solutions',
  'products',
  'components',
]

const SearchMetainfoPage = ({ setExtraIcons }) => {
  const [searchParams, setSearchParams] = useSearchParams()
  const [profile, setProfile] = useState(undefined)
  const [roles, setRoles] = useState(undefined)
  const [statuses, setStatuses] = useState([])
  const [stagedGroupBy, setStagedGroupBy] = useState('date')
  const [activeGroupBy, setActiveGroupBy] = useState('date')
  const [stagedFilters, setStagedFilters] = useState({})
  const [activeFilters, setActiveFilters] = useState({})
  const [isDownloading, setDownloading] = useState(false)

  useEffect(() => {
    setExtraIcons([])
  }, [setExtraIcons])

  useEffect(() => {
    setStatuses(statusesFromSearchParams(searchParams.get('status')))

    const newGroupBy = searchParams.get('groupBy') || 'date'
    setStagedGroupBy(newGroupBy)
    setActiveGroupBy(newGroupBy)

    const newFilters = JSON.parse(searchParams.get('filters') || '{}')
    setStagedFilters(newFilters)
    setActiveFilters(newFilters)
  }, [searchParams])

  useEffect(() => {
    getUserSelf().then(
      result => { setProfile(result) }
    ).catch((error) => {
      setProfile(error)
    })
  }, [])

  useEffect(() => {
    getUserSelfRoles().then(
      result => { setRoles(result) }
    ).catch((error) => {
      setRoles(error)
    })
  }, [])

  const collection = searchParams.get('type')

  return renderState(roles, (roles) => roles.includes(ROLE_PRODUCT_RELEASE) ? (
   <Page>
      <PageContent>
        <PageHeader title={'Metainfo search'} />
        <FormField label='Searching for...'>
          <Select
            options={validMetainfoTypes}
            value={searchParams.get('type') || ''}
            placeholder={'Metainfo type'}
            onChange={({ option }) => setSearchParams({ 'type': option })}
          />
        </FormField>
        {
          validMetainfoTypes.includes(searchParams.get('type')) ?
            <Box>
              <SearchMetainfoStatus collection={collection} allStatuses={statusesForCollection(collection)} activeStatuses={statuses} onChange={event => setStatuses(event.value)} />
              <SearchMetainfoLatestBy collection={collection} value={stagedGroupBy} onChange={event => setStagedGroupBy(event.target.value)} />
              <SearchMetainfoFilters collection={collection} filters={stagedFilters} onFiltersChange={value => { console.log('Staged filters:', value); setStagedFilters({ ...value }) }} />
              <Box direction='row' flex='grow' margin={{ top: 'medium', bottom: 'medium' }}>
                <Button label='Search' fill='horizontal' primary onClick={() => {
                  console.log('Submitted filters:', stagedFilters)
                  setSearchParams({
                    'type': collection,
                    'status': statusesToSearchParams(statuses),
                    'groupBy': stagedGroupBy,
                    'filters': JSON.stringify(stagedFilters),
                  })
                }}
                />
                <Button title='Download search results as CSV' icon={isDownloading ? <Spinner /> : <Download />} onClick={!isDownloading ? () => {
                  setDownloading(true);
                  downloadListArtifactsCsv(collection, 'summary', activeFilters, groupByToAggregateOn[activeGroupBy], null, 2 ** 31, () => {
                    setDownloading(false);
                  })
                } : undefined}
                />
              </Box>
              {
                Object.keys(activeFilters).length !== 0
                  ? <TableArtifactsQueried
                    collection={collection}
                    filters={activeFilters}
                    aggregateOn={groupByToAggregateOn[activeGroupBy]}
                    columns={columnsPerCollection(collection)}
                    displayIf={displayIfStatusFilter(statuses)}
                  />
                  : <Box pad='large'><Text alignSelf='center'>No filters set.</Text></Box>
              }
            </Box>
            : null
        }
      </PageContent>
    </Page>
  ) : (
    <Page>
      <PageContent>
        <PageHeader title={'Metainfo search'} />
        <Text>User not authorized</Text>
      </PageContent>
    </Page>
  ));  
  }

export default SearchMetainfoPage
