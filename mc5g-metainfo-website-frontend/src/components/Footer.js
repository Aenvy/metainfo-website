import { useContext } from 'react'
import {
  Box,
  Button,
  Footer,
  ResponsiveContext,
  Text,
} from 'grommet'

import { metainfoApiUrl } from '../config'

const Footer5GIntegration = () => {
  const size = useContext(ResponsiveContext);
  const year = new Date().getFullYear();

  return (
    <Footer
      background="background-front"
      direction={!['xsmall', 'small'].includes(size) ? 'row' : 'column'}
      align={!['xsmall', 'small'].includes(size) ? 'center' : undefined}
      justify={!['xsmall', 'small'].includes(size) ? 'between' : undefined}
      pad={{ horizontal: 'medium', vertical: 'small' }}
      fill="horizontal"
    >
      <Box
        direction={!['xsmall', 'small'].includes(size) ? 'row' : 'column'}
        align={!['xsmall', 'small'].includes(size) ? 'center' : undefined}
        gap="xsmall"
      >
        <Text size="small">
          &copy; {year} Hewlett Packard Enterprise Development LP
        </Text>
        <Box
          direction="row"
          align={!['xsmall', 'small'].includes(size) ? 'center' : undefined}
          gap="xsmall"
          wrap
        >
          <a href={`${metainfoApiUrl}/swagger-ui`} target='_blank' rel='noopener noreferrer'><Button label='API documentation' /></a>
        </Box>
      </Box>
      <Box
	      direction="row"
        align="center"
        gap="xsmall"
        wrap
      >
        <Text size="small">For bug reports and feature ideas, use the Website v2 workflow in <a href='https://hpe.enterprise.slack.com/archives/C027HFRAR36' target='_blank' rel='noopener noreferrer'><Button label='#ask-siths' /></a></Text>
      </Box>
    </Footer >
  )
}

export default Footer5GIntegration
