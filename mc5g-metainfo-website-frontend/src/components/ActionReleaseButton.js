import { Button } from 'grommet'
import { CloudUpload } from 'grommet-icons'

const ActionReleaseButton = ({ onClick }) => {
  return (
    <Button icon={<CloudUpload />} title='Release...' onClick={event => onClick(event)} />
  )
}

export default ActionReleaseButton
