import { Text } from 'grommet'

import MetainfoTestResultTestSuites from './MetainfoResultTestSuites'
import TableArtifacts from './TableArtifacts'

const COLLECTION = 'results'
const COLUMNS = ['name', 'ident.version', 'testType', 'status']

const MetainfoResultFor = ({ metainfos }) => {
  return (
    <TableArtifacts
      collection={COLLECTION}
      data={metainfos}
      columns={COLUMNS}
      rowDetails={
        item => item.testSuites
          ? <MetainfoTestResultTestSuites data={Object.values(item.testSuites)} />
          : <Text>No test suites data.</Text>
      } />
  )
}

export default MetainfoResultFor
