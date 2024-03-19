import { Button } from 'grommet'
import { Download } from 'grommet-icons'

import { metainfoApiUrl } from '../config'

const ActionDownloadMetainfoButton = ({ collection, groupId, artifactId, version }) => {
  return (
    <a href={`${metainfoApiUrl}/${collection}/${groupId}/${artifactId}/${version}?raw=true`} target='_blank' rel='noreferrer'>
      <Button icon={<Download />} title='Download metainfo' />
    </a>
  )
}

export default ActionDownloadMetainfoButton
