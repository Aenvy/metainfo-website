import {
  DataTable,
  Text,
} from 'grommet'

const columns = [
  {
    header: 'Type',
    property: 'type',
  },
  {
    header: 'Date',
    property: 'date',
  },
  {
    header: 'Details',
    property: 'details'
  },
  {
    header: 'Job',
    property: 'job',
    render: datum => (
      datum.job && datum.job.id ? <a href={datum.job.url} target='_blank' rel='noreferrer'>Build #{datum.job.id}</a> : null
    )
  },
]

const MetainfoHistory = ({ history }) => {
  if (!Array.isArray(history) || history.length === 0) {
    return <Text>None.</Text>
  }

  return (
    <DataTable
      columns={columns}
      data={history}
      primaryKey='_key'
    />
  )
}

export default MetainfoHistory
