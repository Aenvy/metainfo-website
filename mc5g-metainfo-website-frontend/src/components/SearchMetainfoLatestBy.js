import {
  FormField,
  RadioButtonGroup,
} from 'grommet'

const groupByStatesSolutions = [
  {
    'label': 'Version',
    'value': 'version',
  },
  {
    'label': 'Date',
    'value': 'date',
  },
  {
    'label': 'All',
    'value': 'nothing',
  }
]

const groupByStates = [
  {
    'label': 'Branch',
    'value': 'branch',
  },
  {
    'label': 'Version',
    'value': 'version',
  },
  {
    'label': 'Date',
    'value': 'date',
  },
  {
    'label': 'All',
    'value': 'nothing',
  }
]

const SearchMetainfoLatestBy = ({ collection, value, onChange }) => {
  return (
    <FormField label='Show latest by...'>
      <RadioButtonGroup
        name='groupBy'
        value={value}
        options={collection === 'solutions' ? groupByStatesSolutions : groupByStates}
        onChange={onChange}
      />
    </FormField>
  )
}

export default SearchMetainfoLatestBy
