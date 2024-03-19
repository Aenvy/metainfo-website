import {
  Box,
  PageHeader,
  Tag,
  Text,
} from 'grommet'
import { Link } from 'react-router-dom'

const MetainfoHeader = ({ collection, metainfo }) => {
  return (
    <Box>
      <Box direction="row">
        <PageHeader title={metainfo.name} subtitle={metainfo.description} flex="grow" />
        <Box alignSelf="center">
          <Text style={{ whiteSpace: "nowrap" }}>{metainfo.ident.groupId}</Text>
          <Text style={{ whiteSpace: "nowrap" }}><Link to={`/${collection}/${metainfo.ident.groupId}/${metainfo.ident.artifactId}`}>{metainfo.ident.artifactId}</Link></Text>
          <Text style={{ whiteSpace: "nowrap" }}>{metainfo.ident.version}</Text>
          <Text style={{ whiteSpace: "nowrap" }}>{metainfo.scm && metainfo.scm.branch}</Text>
        </Box>
      </Box>
      <Box direction='row' alignSelf='end' wrap={true} >{
        metainfo.tags && metainfo.tags.map(item => <Tag value={item} key={item} />)
      }</Box>
    </Box>
  )
}

export default MetainfoHeader
