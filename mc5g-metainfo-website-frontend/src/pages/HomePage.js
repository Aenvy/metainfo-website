import React from 'react';
import { Page, PageContent, Box, Heading, Button } from 'grommet';
import { Link } from 'react-router-dom';
import { Cubes, Cube, Document, Catalog } from 'grommet-icons';

const Dashboard = () => {
  return (
    <Page>
      <PageContent>
        <Box align="center">
          <Heading level={1}>Welcome to the {process.env.REACT_APP_WEBSITE_COMPANY_NAME} {process.env.REACT_APP_WEBSITE_NAME} website</Heading>
        </Box>
        <Box direction="row" justify="center" gap="medium">
          <Link to="/solutions">
            <Button icon={<Cubes size='xlarge' />} label="Solutions" primary />
          </Link>
          <Link to="/products">
            <Button icon={<Cube size='xlarge' />} label="Products" primary />
          </Link>
          <Link to="/components">
            <Button icon={<Document size='xlarge' />} label="Components" primary />
          </Link>
          <Link to="/releases">
            <Button icon={<Catalog size='xlarge' />} label="Releases" primary />
          </Link>
        </Box>
      </PageContent>
    </Page>
  );
}

export default Dashboard;
