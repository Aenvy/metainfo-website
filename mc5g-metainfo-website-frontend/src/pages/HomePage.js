import React from 'react';
import { Page, PageContent, Box, Heading, Button, Tip, Text } from 'grommet';
import { Link } from 'react-router-dom';
import { Cubes, Cube, Document, Catalog, HelpOption } from 'grommet-icons';

const Dashboard = () => {
  return (
    <Page>
      <PageContent>
        <Box align="center">
          <Heading level={1}>Welcome to the {process.env.REACT_APP_WEBSITE_COMPANY_NAME} {process.env.REACT_APP_WEBSITE_NAME} website</Heading>
        </Box>
        <Box direction="row" justify="center" gap="medium">
          <Box align="center" border={{size: 'small' }} pad="small" round="small">
            <Link to="/solutions">
              <Button icon={<Cubes size='xlarge' />} label="Solutions" primary />
            </Link>
            <Tip content={
              <Box pad="small">
                <Text>- HPE CMS 5G Interworking solution</Text>
                <Text>- HPE CMS 5G Storage Proxy solution (for CIHSS)</Text>
                <Text>- HPE CMS 5G Integration solution</Text>
              </Box>
            }>
              <Box align="center">
                <HelpOption />
              </Box>
            </Tip>
          </Box>
          <Box align="center" border={{size: 'small' }} pad="small" round="small">
            <Link to="/products">
              <Button icon={<Cube size='xlarge' />} label="Products" primary />
            </Link>
            <Tip content={
              <Box pad="small">
                <Text>- HPE 5GC AUSF</Text>
                <Text>- HPE 5GC NHSS</Text>
                <Text>- HPE 5GC 5G-EIR</Text>
                <Text>- HPE 5GC UDR</Text>
                <Text>- HPE 5GC UDM</Text>
                <Text>- HPE 5GC PGW</Text>
                <Text>- HPE 5GC UDSF</Text>
                <Text>- ... and more</Text>
              </Box>
            }>
              <Box align="center">
                <HelpOption />
              </Box>
            </Tip>
          </Box>
          <Box align="center" border={{size: 'small' }} pad="small" round="small">
            <Link to="/components">
              <Button icon={<Document size='xlarge' />} label="Components" primary />
            </Link>
            <Tip content={
              <Box pad="small">
                <Text>- hpe-nf-ausf-oam-comp</Text>
                <Text>- hpe-nf-nrf-notify-agent-comp</Text>
                <Text>- hpe-nf-operator-comp</Text>
                <Text>- hpe-nf-operator-deployment-comp</Text>
                <Text>- 5G Solution Prerequisite component</Text>
                <Text>- hpe-nf-nudm-notify-comp</Text>
                <Text>- hpe-nf-nudm-prov-comp</Text>
                <Text>- ... and more</Text>
              </Box>
            }>
              <Box align="center">
                <HelpOption />
              </Box>
            </Tip>
          </Box>
          <Box align="center" border={{size: 'small' }} pad="small" round="small">
            <Link to="/releases">
              <Button icon={<Catalog size='xlarge' />} label="Releases" primary />
            </Link>
            <Tip content={
              <Box pad="small">
                <Text>- Release Candidates</Text>
                <Text>- GA Releases</Text>
              </Box>
            }>
              <Box align="center">
                <HelpOption />
              </Box>
            </Tip>
          </Box>
        </Box>
      </PageContent>
    </Page>
  );
}

export default Dashboard;
