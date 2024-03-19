import {
  Box,
  DataTable,
  Tag,
  Text,
} from 'grommet'
import {
  Checkmark,
} from 'grommet-icons'
import {
  useEffect,
  useState,
} from 'react'
import { Link } from 'react-router-dom'

import {
  compareVersion,
  datumValue,
} from '../utils'

const DEFAULT_SORT = {
  direction: 'desc',
  property: 'ident.version',
}

const DEFAULT_COLUMNS = [
  'name',
  'ident.version',
  'status',
]

function sortArtifacts(artifacts, { property, direction }) {
  var sortFn = undefined
  if (property === 'discarded') {
    sortFn = (d1, d2) => (d1.status !== 'Discarded') - (d2.status !== 'Discarded')
  } else if (property === 'ident.version') {
    sortFn = compareVersion
  } else if (property === 'tags') {
    sortFn = (d1, d2) => ((d1.tags || []).length - (d2.tags || []).length)
  } else {
    sortFn = (d1, d2) => (datumValue(d1, property) || '').localeCompare(datumValue(d2, property) || '', undefined, { sensitivity: 'base' })
  }

  artifacts.sort(sortFn)
  if (direction === 'desc') {
    artifacts.reverse()
  }
}

const TableArtifacts = ({ collection, columns, sortable, data, rowDetails, sort, nested=false, nestedPrefix='' }) => {
  const [sortedVersions, setSortedVersions] = useState(data)

  useEffect(() => {
    sortable && sortArtifacts(data, sort || DEFAULT_SORT)
    setSortedVersions(data.map(datum => { return {...datum, '_key': `${datum.ident.groupId}/${datum.ident.artifactId}/${datum.ident.version}`} }))
  }, [collection, sortable, data, sort])

  const allColumns = [
    {
      header: 'Name',
      property: 'name',
      render: datum => (
        <Link to={`/${collection}/${datum.ident.groupId}/${datum.ident.artifactId}`}>{datum.name}</Link>
      ),
    },
    {
      header: 'Description',
      property: 'description',
    },
    {
      header: 'Group ID',
      property: 'ident.groupId',
    },
    {
      header: 'Artifact ID',
      property: 'ident.artifactId',
      render: datum => (
        <Link to={`/${collection}/${datum.ident.groupId}/${datum.ident.artifactId}`}>{datum.ident.artifactId}</Link>
      ),
    },
    {
      header: 'Version',
      property: 'ident.version',
      render: datum => {
        const version = datum.ident.version;
        const regex_lastpart = /-\d{1,2}$/;
    
        if (regex_lastpart.test(version)) {
          const version_to_display = version.replace(regex_lastpart, '');
          
          return (
            
            <Link to={`${nested ? nestedPrefix : '/'}${collection}/${datum.ident.groupId}/${datum.ident.artifactId}/${datum.ident.version}`}>{version_to_display}</Link>
          );
        } else {
          return (
            <Link to={`${nested ? nestedPrefix : '/'}${collection}/${datum.ident.groupId}/${datum.ident.artifactId}/${datum.ident.version}`}>{version}</Link>
          );
        }
      }
    },
    
    {
      header: 'Test type',
      property: 'testType',
    },
    {
      header: 'Status',
      property: 'status',
      render: datum => (
        datum.status && datum.status.includes('Failed')
          ? <Box background='red'>{datum.status}</Box>
          : datum.status
      ),
    },
    {
      header: 'Branch',
      property: 'scm.branch',
    },
    {
      header: 'Tags',
      property: 'tags',
      render: data => (
        Array.isArray(data.tags)
          ? <Box>{data.tags.map(datum => <Tag key={datum} value={datum} />)}</Box>
          : null
      ),
    },
    {
      header: 'Discarded',
      property: 'discarded',
      render: datum => datum.status === 'Discarded' ? <Checkmark /> : null,
    },
  ]

  return (
    data.length !== 0
      ? (sortable
          ? <DataTable
            columns={allColumns.filter(i => (columns ? columns : DEFAULT_COLUMNS).includes(i.property))}
            data={sortedVersions}
            rowDetails={rowDetails}
            sort={{...sort || DEFAULT_SORT, external: true}}
            onSort={(o) => {
              sortArtifacts(data, o)
              setSortedVersions(data)
            }}
            sortable={true}
            primaryKey={'_key'} />
          : <DataTable
            columns={allColumns.filter(i => (columns ? columns : DEFAULT_COLUMNS).includes(i.property))}
            data={data}
            rowDetails={rowDetails}
            primaryKey={'_key'} />)
      : <Text>None.</Text>
  )
}

export default TableArtifacts
