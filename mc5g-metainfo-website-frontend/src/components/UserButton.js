import {
  Box,
  Button,
  DropButton,
 } from 'grommet'
import {
  Login,
  Logout,
  User,
} from 'grommet-icons'

import { login, logout } from '../api/user'

const UserButton = ({ profile }) => {
  if (profile['id']) {
    return (
      <DropButton label={profile['name']} icon={<User />} dropAlign={{top: 'bottom'}} dropContent={
        <Box>
          <Button icon={<Logout />} label='Logout' onClick={event => logout()} />
        </Box>
      } />
    )
  } else {
    return <Button icon={<Login />} title='Login' onClick={event => login()} />
  }
}

export default UserButton
