import {
  Button,
  DataTable,
  Text,
} from 'grommet'
import { Download } from 'grommet-icons'

function formatDeliverable(deliverable) {
  if (!deliverable || !Array.isArray(deliverable.media)) {
    return []
  }

  return deliverable.media.map(medium => {
    const server = deliverable.servers[medium.servers[0]]
    const url = (server.slice(-1) === '/') ? `${server}${medium.name}` : `${server}/${medium.name}`

    return {
      type: medium.type,
      name: medium.name,
      button: <Button title='Download deliverable'><a href={url} target='_blank' rel='noreferrer'><Download /></a></Button>
    }
  })
}

const columns = [
  {
    header: 'Type',
    property: 'type',
  },
  {
    header: 'Name',
    property: 'name',
  },
  {
    header: 'Link',
    property: 'button',
    align: 'center',
  },
]

const MetainfoDeliverable = ({ deliverable }) => {
  const formattedDeliverable = formatDeliverable(deliverable)
  if (formattedDeliverable.length === 0) {
    return <Text>None.</Text>
  }

  return (
    <DataTable
      columns={columns}
      data={formattedDeliverable}
    />
  )
}

export default MetainfoDeliverable
