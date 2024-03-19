import {
  Box,
} from 'grommet'
import { Link } from 'react-router-dom'

import TableArtifacts from './TableArtifacts'

const MetainfoRelated = ({ collection, data, moreLink }) => {
  return (
    <Box>
        <TableArtifacts collection={collection} data={data.members} />
        {
          data.count < data.total ? <Link to={moreLink}>More...</Link> : null
        }
    </Box>
  )
}

export default MetainfoRelated
