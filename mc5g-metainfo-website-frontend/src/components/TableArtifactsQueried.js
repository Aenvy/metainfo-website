import {
  useEffect,
  useState,
} from 'react'

import { getListArtifacts } from '../api/metainfo'
import { renderState } from '../utils'

import TableArtifacts from './TableArtifacts'

const TableArtifactsQueried = ({ collection, filters, aggregateOn, columns, displayIf, sort }) => {
  const [versions, setVersions] = useState(undefined)
  const [data, setData] = useState(undefined)

  useEffect(() => {
    setVersions(undefined)

    getListArtifacts(collection, 'summary', filters, aggregateOn).then(
      result => setVersions(result)
    ).catch((error) => {
      setVersions(error)
    })
  }, [collection, filters, aggregateOn])

  useEffect(() => {
    if (versions && Array.isArray(versions.members)) {
      if (displayIf) {
        setData(versions.members.slice().filter(item => displayIf(item)))
      } else {
        setData(versions.members)
      }
    } else {
      setData(versions)
    }
  }, [versions, displayIf])

  return (
    renderState(data, (data) =>
      <TableArtifacts
        collection={collection}
        columns={columns}
        data={data}
        sortable={true}
        sort={sort}
      />
    )
  )
}

export default TableArtifactsQueried
