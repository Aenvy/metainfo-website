import {
  Box,
  PageContent,
  Text,
} from 'grommet'
import {
  useEffect,
} from 'react'

import { renderState } from '../utils'

import TableArtifacts from '../components/TableArtifacts'

const LatestReleasesView = ({ setExtraIcons, releases, nested=false, ...props }) => {
  useEffect(() => {
    setExtraIcons([])
  }, [setExtraIcons])

  return (
    <PageContent {...props}><h1>Latest releases</h1>{
      renderState(releases, (releases) =>
        releases.map(release =>
          <Box key={release.release}>
            <a href={`#${release.release.replace(/\./g, '_')}`} id={release.release.replace(/\./g, '_')}>
            {
              release.release.match(/RC/)
                ? <Box><Text margin='small' size='large' weight='bolder' color='orange'>{release.release}</Text></Box>
                : <Box><Text margin='small' size='large' weight='bolder' color='green'>{release.release}</Text></Box>
            }
            </a>
            <TableArtifacts collection='products' data={release.products} sortable={true} sort={{ direction: 'asc', property: 'name' }} nested={nested} nestedPrefix={`${release.release}/`} />
          </Box>
        )
      )
    }</PageContent>
  )
}

export default LatestReleasesView
