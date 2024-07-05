import React, { useContext } from 'react';
import { Grommet, Box, Page } from 'grommet';
import { hpe } from 'grommet-theme-hpe';
import { Outlet } from 'react-router-dom';

import Footer from '../components/Footer';
import Header from '../components/Header';
import { ThemeContext } from '../ThemeContext';

// Theme-like object specifying alignment, width, and spacing for
// an AppContainer.
const appContainer = {
  gap: 'large',
  width: {
    min: 'medium',
  },
};

const AppContainer = ({ extraIcons }) => {
  const { theme } = useContext(ThemeContext);

  const customTheme = {
    ...hpe,
    global: {
      ...hpe.global,
      colors: {
        ...hpe.global.colors,
        background: theme === 'light' ? '#ffffff' : '#2c2c2c',
        text: theme === 'light' ? '#000000' : '#ffffff',
        link: theme === 'light' ? '#0073e6' : '#80bdff',
        linkHover: theme === 'light' ? '#005bb5' : '#66a3ff',
      },
    },
  };

  return (
    <Grommet theme={customTheme} gap={appContainer.gap}
    style={{minHeight: '100vh', display: 'flex', flexDirection: 'column'}}>
      <Header extraIcons={extraIcons} />
      <Page style={{flex: 1}}>
        <Outlet />
      </Page>
      <Footer />
    </Grommet>
  );
};

export default AppContainer;
