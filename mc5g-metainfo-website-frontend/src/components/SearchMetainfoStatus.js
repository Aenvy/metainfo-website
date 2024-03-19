import { Box, FormField, SelectMultiple } from 'grommet';
import {
  renderState 
} from '../utils'
import {
  useEffect,
  useState,
} from 'react'
import {
  ROLE_PRODUCT_RELEASE,
  getUserSelf,
  getUserSelfRoles,
} from '../api/user'

const SearchMetainfoStatus = ({ allStatuses, activeStatuses, onChange }) => {
  const [profile, setProfile] = useState(undefined)
  const [roles, setRoles] = useState(undefined)

  useEffect(() => {
    getUserSelfRoles().then(
      result => { setRoles(result) }
    ).catch((error) => {
      setRoles(error)
    })
  }, [])
  return renderState(roles, (roles) => roles.includes(ROLE_PRODUCT_RELEASE) ? (
    <Box>
      <FormField label='With status...'>
        <SelectMultiple
          placeholder={activeStatuses.length > 0 ? allStatuses.filter(status => activeStatuses.includes(status)).join(', ') : 'Any'}
          options={allStatuses}
          value={activeStatuses}
          onChange={onChange}
        />
      </FormField>
    </Box>
  ) : null);
};

export default SearchMetainfoStatus;
