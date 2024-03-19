import {
  Page,
} from 'grommet'

import NotFoundView from '../views/NotFoundView'

const NotFoundPage = ({ setExtraIcons }) => {
  return (
    <Page>
      <NotFoundView setExtraIcons={setExtraIcons} />
    </Page>
  )
}

export default NotFoundPage
