import { useContext } from 'react'
import {
  Box,
  Button,
  Footer,
  ResponsiveContext,
  Text,
} from 'grommet'
import { Link } from 'react-router-dom';

import { metainfoApiUrl } from '../config'

const Footer5GIntegration = () => {
  const size = useContext(ResponsiveContext);
  const year = new Date().getFullYear();

  return (
    <Footer
      background="background-front"
      direction="row"
      align="center"
      justify="between" // This spreads out the child boxes
      pad={{ horizontal: 'medium', vertical: 'small' }}
      fill="horizontal"
    >
      {/* Left-aligned content */}
      <Box align="center" gap="small" direction="row">
        <Text size="small">
          &copy; {year} Hewlett Packard Enterprise Development LP
        </Text>
        <a href={`${metainfoApiUrl}/swagger-ui`} target='_blank' rel='noopener noreferrer'>
          <Button label='API documentation' />
        </a>
      </Box>

      {/* Centered content */}
      <Box align="center" gap="small">
        <Link to="/release-notes"><Button label="Release Notes" /></Link>
      </Box>

      {/* Right-aligned content */}
      <Box align="center" gap="small">
        <Text size="small">
          For bug reports and feature ideas, use the Website v2 workflow in 
          <a href='https://hpe.enterprise.slack.com/archives/C027HFRAR36' target='_blank' rel='noopener noreferrer'><Button label= '#ask-siths' /></a>
        </Text>
      </Box>
    </Footer>
  );
}

export default Footer5GIntegration
