import {
  Box,
  Button,
  DataTable,
  Text,
} from 'grommet'
import {
  Checkmark,
  Close,
  Download
} from 'grommet-icons'

function formatTestCampaigns(testCampaigns) {
  if (!Array.isArray(testCampaigns)) {
    return []
  }

  return testCampaigns.map(campaign => {
    for (const category of campaign.categories) {
      const name = category.name.toLowerCase()

      if (category.status === 'passed') {
        campaign[name] = <Box align='center'><Checkmark /></Box>
      } else if (category.status === 'failed') {
        campaign[name] = <Box align='center'><Close /></Box>
      } else {
        campaign[name] = <Text textAlign='center'>{category.status}</Text>
      }
    }

    return campaign
  })
}

const categoryStyle = {
  display: 'flex',
  justifyContent: 'center',
  alignItems: 'center',
  writingMode: 'vertical-rl',
}

const columns = [
  {
    header: 'Title',
    property: 'title',
  },
  {
    header: 'Description',
    property: 'description',
  },
  {
    header: 'Date',
    property: 'date',
  },
  {
    header: <Text style={categoryStyle}>Deployment</Text>,
    property: 'deployment',
  },
  {
    header: <Text style={categoryStyle}>Endurance</Text>,
    property: 'endurance',
  },
  {
    header: <Text style={categoryStyle}>Performance</Text>,
    property: 'performance',
  },
  {
    header: <Text style={categoryStyle}>Robustness</Text>,
    property: 'robustness',
  },
  {
    header: <Text style={categoryStyle}>Stress</Text>,
    property: 'stress',
  },
  {
    header: <Text style={categoryStyle}>Operations</Text>,
    property: 'operations',
  },
  {
    header: <Text style={categoryStyle}>Upgrade</Text>,
    property: 'upgrade',
  },
  {
    header: <Text style={categoryStyle}>Usability</Text>,
    property: 'usability',
  },
  {
    header: <Text style={categoryStyle}>Supportability</Text>,
    property: 'supportability',
  },
  {
    header: 'Link',
    property: 'link',
    render: datum => (
      <Button title='Download test report'>
        <a href={datum.link} target='_blank' rel='noreferrer'>
          <Download />
        </a>
      </Button>
    )
  },
]

const MetainfoTestCampaigns = ({ testCampaigns }) => {
  const formattedTestCampaigns = formatTestCampaigns(testCampaigns)
  if (formattedTestCampaigns.length === 0) {
    return <Text>None.</Text>
  }

  return (
    <DataTable
      columns={columns}
      data={formattedTestCampaigns}
    />
  )
}

export default MetainfoTestCampaigns
