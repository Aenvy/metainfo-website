import { DataTable } from 'grommet'
import { Checkmark } from 'grommet-icons'

const format = require('format-duration')

const MetainfoResultTestSuites = ({ data }) => {
  const allColumns = [
    {
      header: 'Feature',
      property: 'feature',
    },
    {
      header: 'Duration',
      property: 'duration',
      render: datum => format(datum.duration * 1000, { ms: true })
    },
    {
      header: 'Failed tests',
      property: 'results.failedTests',
    },
    {
      header: 'Total tests',
      property: 'results.testCount',
    },
    {
      header: 'Passed',
      property: 'results.passRate',
      render: datum => datum.results.passRate === 1 ? <Checkmark /> : null,
    },
  ]

  return (
    <DataTable
      columns={allColumns}
      data={data}
    />
  )
}

export default MetainfoResultTestSuites
