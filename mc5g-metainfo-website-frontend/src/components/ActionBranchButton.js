import { Button } from 'grommet'
import { Network } from 'grommet-icons'

const ActionBranchButton = ({ onClick }) => {
  return (
    <Button icon={<Network />} title='Branch...' onClick={event => onClick(event)} />
  )
}

export default ActionBranchButton
