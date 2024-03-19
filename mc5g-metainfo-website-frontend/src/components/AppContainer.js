import {
  Grommet,
  Page,
} from 'grommet'
import { hpe } from 'grommet-theme-hpe'
import { Outlet } from 'react-router-dom'

import Footer from '../components/Footer'
import Header from '../components/Header'

// Theme-like object specifying alignment, width, and spacing for
// an AppContainer.
const appContainer = {
  gap: "large",
  width: {
    min: "medium",
  },
}

const AppContainer = ({ extraIcons }) => (
  <Grommet theme={hpe}
    gap={appContainer.gap}
    style={{minHeight: '100vh', display: 'flex', flexDirection: 'column'}}>
      <Header extraIcons={extraIcons} />
      <Page style={{flex: 1}}>
        <Outlet />
      </Page>
      <Footer />
  </Grommet>
)

export default AppContainer
