import {
  Box,
  Button,
  Header,
  Nav,
  Text,
} from 'grommet'
import {
  Cubes,
  Cube,
  Document,
  Hpe,
  Search,
  Catalog
} from 'grommet-icons'
import {
  useEffect,
  useState
} from 'react'

import { Link, useNavigate } from 'react-router-dom'

import {
  ROLE_COMPONENT_LIST,
  ROLE_PRODUCT_LIST,
  ROLE_SOLUTION_LIST,
  ROLE_PRODUCT_RELEASE,
  getUserSelf,
  getUserSelfRoles,
} from '../api/user'
import { renderStateIcon } from '../utils'

import UserButton from './UserButton'

/*const ROLES_FOR_SEARCH=[
  ROLE_COMPONENT_LIST,
  ROLE_PRODUCT_LIST,
  ROLE_SOLUTION_LIST,
]*/

const Header5GIntegration = ({ extraIcons }) => {
  const [profile, setProfile] = useState(undefined)
  const [roles, setRoles] = useState(undefined)
  const history = useNavigate()

  useEffect(() => {
    getUserSelf().then(
      result => { setProfile(result) }
    ).catch((error) => {
      setProfile(error)
    })
  }, [])

  useEffect(() => {
    getUserSelfRoles().then(
      result => { setRoles(result) }
    ).catch((error) => {
      setRoles(error)
    })
  }, [])

  const handleHomeButtonClick = () => {
    history.push('/'); // Navigate to the home page
    window.location.reload(); // Refresh the page
  }

  return (
    <Header fill="horizontal">
      <Link to="/" onClick={handleHomeButtonClick}>
        <Button title="Home">
          <Box
            direction="row"
            align="start"
            gap="small"
            pad={{ left: "xsmall", vertical: "small" }}
            responsive={false}
          >
            <Hpe color="brand" />
            <Box direction="row" gap="xsmall" wrap>
              <Text color="text-strong" weight="bold">{process.env.REACT_APP_WEBSITE_COMPANY_NAME}</Text>
              <Text color="text-strong">{process.env.REACT_APP_WEBSITE_NAME}</Text>
            </Box>
          </Box>
        </Button>
      </Link>
      <Nav direction="row" gap="none">
        {
          Array.isArray(extraIcons) ? extraIcons.slice().reverse().map((extraIcon, index) => <Box key={`${index}-${extraIcon}`}>{extraIcon}</Box>) : null
        }
        {
          Array.isArray(extraIcons) && extraIcons.length > 0 ? <hr style={{'borderStyle': 'solid'}}/> : null
        }
        {
          renderStateIcon(roles, (roles) => roles.includes(ROLE_PRODUCT_RELEASE) ? <Link to="/search"><Button icon={<Search />} title="Search" /></Link> : null)
        }
        {
          renderStateIcon(roles, (roles) => roles.includes(ROLE_SOLUTION_LIST) ? <Link to="/solutions"><Button icon={<Cubes />} title="Solutions" /></Link> : null)
        }
        {
          renderStateIcon(roles, (roles) => roles.includes(ROLE_PRODUCT_LIST) ? <Link to="/products"><Button icon={<Cube />} title="Products" /></Link> : null)
        }
        {
          renderStateIcon(roles, (roles) => roles.includes(ROLE_COMPONENT_LIST) ? <Link to="/components"><Button icon={<Document />} title="Components" /></Link> : null)
        }
        {
          renderStateIcon(roles, (roles) => roles.includes(ROLE_SOLUTION_LIST) ? <Link to="/releases"><Button icon={<Catalog />} title="Releases" /></Link> : null)
        }
        {
          renderStateIcon(profile, (profile) => <UserButton profile={profile} />)
        }
      </Nav>
    </Header>
  )
}

export default Header5GIntegration
