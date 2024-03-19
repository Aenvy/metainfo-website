import {
  useEffect,
  useState,
} from 'react'
import {
  Box,
  Button,
  CheckBox,
  FormField,
  Grid,
  Menu,
  Select,
  Text,
  TextInput,
} from 'grommet'
import {
  Add,
  Trash,
} from 'grommet-icons'

import { getCollectionSchema } from '../api/metainfo'

import { renderState } from '../utils'

function defaultValueFor(schema) {
  if (schema['type'] === 'string') {
    return ''
  } else if (schema['type'] === 'boolean') {
    return false
  } else if (schema['type'] === 'array') {
    return {'$allOf': []}
  } else if (typeof schema['type'] === 'object') {
    return {}
  }
}

function getOperatorFromQuery(operatorTests, query) {
  return Object.entries(operatorTests).filter(([key, value]) => value(query)).map(item => item[0])[0]
}

function propertyToWidget(path, key, value, schema, onUpdateFilter) {
  const fullPath = path.join('.')

  const valueWrapper = (child) =>
    <SearchWidgetField key={fullPath} label={key} path={path} onUpdateFilter={onUpdateFilter}>
      {child}
    </SearchWidgetField>

  if (schema['type'] === 'array') {
    return valueWrapper(<SearchWidgetArrayOperator path={path} query={value} schema={schema['subtype']} onUpdateFilter={onUpdateFilter} />)
  } else if (schema['type'] === 'string') {
    return valueWrapper(<SearchWidgetStringOperator path={path} query={value} onUpdateFilter={onUpdateFilter} />)
  } else if (schema['type'] === 'boolean') {
    return valueWrapper(<SearchWidgetBoolean path={path} query={value} onUpdateFilter={onUpdateFilter} />)
  } else if (typeof schema['type'] === 'object') {
    return valueWrapper(<SearchWidgetObjectKeys path={path} query={value} schema={schema['type']} onUpdateFilter={onUpdateFilter} />)
  }
}

const SearchWidgetField = ({label, path, onUpdateFilter, children}) => {
  const shouldHaveLabel = isNaN(parseInt(label))

  return (
    <Grid columns={shouldHaveLabel ? ['125px', 'flex', 'auto'] : ['flex', 'auto']}>
      {
        shouldHaveLabel ? <Box alignSelf='center'><Text>{label}</Text></Box> : null
      }
      {
        children
      }
      <Button icon={<Trash />} title='Remove property' onClick={event => onUpdateFilter(path, undefined)} />
    </Grid>
  )
}

const SearchWidgetObjectKeys = ({ path, query, schema, onUpdateFilter }) => {
  const addPropertyValues = Object.keys(schema).filter(item => !Object.keys(query).includes(item))
  const addPropertyItems = addPropertyValues.map(value => { return {
    label: value,
    onClick: event => onUpdateFilter([...path, value], defaultValueFor(schema[value]))
  }})

  return (
    <Box pad={'small'}>
      {
        Object.entries(query).map(([key, value]) => propertyToWidget([...path, key], key, value, schema[key], onUpdateFilter))
      }
      {
        addPropertyItems.length > 0
          ? <Menu label='Add property...' items={addPropertyItems} />
          : null
      }
    </Box>
  )
}

const SearchWidgetArrayOperatorCommon = ({ path, operator, query, schema, onUpdateFilter }) => {
  return (
    <Box>
      {
        Object.entries(query[operator]).map(([index, item]) => propertyToWidget([...path, operator, parseInt(index)], index, item, schema, onUpdateFilter))
      }
      <Button icon={<Add />} label='Add clause' onClick={event => onUpdateFilter([...path, operator, query[operator].length], defaultValueFor(schema))}/>
    </Box>
  )
}

const SearchWidgetArrayAllOf = ({ path, query, schema, onUpdateFilter }) => {
  return SearchWidgetArrayOperatorCommon({path, operator: '$allOf', query, schema, onUpdateFilter})
}

const SearchWidgetArrayAnyOf = ({ path, query, schema, onUpdateFilter }) => {
  return SearchWidgetArrayOperatorCommon({path, operator: '$anyOf', query, schema, onUpdateFilter})
}

const SearchWidgetArrayOperator = ({ path, query, schema, onUpdateFilter }) => {
  const opAllOf = 'All of'
  const opAnyOf = 'Any of'

  const operators = [opAllOf, opAnyOf]

  const operatorToWidget = {
    [opAllOf]: SearchWidgetArrayAllOf,
    [opAnyOf]: SearchWidgetArrayAnyOf,
  }
  const operatorToOp = {
    [opAllOf]: '$allOf',
    [opAnyOf]: '$anyOf',
  }
  const operatorTest = {
    [opAllOf]: (query) => Array.isArray(query['$allOf']),
    [opAnyOf]: (query) => Array.isArray(query['$anyOf']),
  }

  const operator = getOperatorFromQuery(operatorTest, query)

  const setValue = (event) => {
    const savedQuery = query[operatorToOp[operator]]
    onUpdateFilter([...path, operatorToOp[operator]], undefined)
    onUpdateFilter([...path, operatorToOp[event.target.value]], savedQuery)
  }

  return (
    <Box>
      <Select options={operators} value={operator} onChange={setValue} />
      {
        operatorToWidget[operator]({path, query, schema, onUpdateFilter})
      }
    </Box>
  )
}

const SearchWidgetStringEqualTo = ({ path, query, schema, onUpdateFilter }) => {
  return (
    <TextInput value={query || ''} onChange={event => onUpdateFilter(path, event.target.value)} />
  )
}

const SearchWidgetStringMatches = ({ path, query, schema, onUpdateFilter }) => {
  return (
    <TextInput value={query.slice(1, -1)} onChange={event => onUpdateFilter(path, `/${event.target.value}/`)} />
  )
}

const SearchWidgetStringOperator = ({ path, query, schema, onUpdateFilter }) => {
  const opEqualTo = 'Equal to'
  const opMatches = 'Matches'
  //const opIn = 'In'
  //const opNotIn = 'Not in'

  const isOpMatches = (query) => typeof query === 'string' && query.length >= 2 && query.startsWith('/') && query.endsWith('/')
  const isOpEqualTo = (query) => typeof query === 'string' && !isOpMatches(query)

  const operators = [opEqualTo, opMatches]

  const operatorToWidget = {
    [opEqualTo]: SearchWidgetStringEqualTo,
    [opMatches]: SearchWidgetStringMatches,
  }
  const operatorTest = {
    [opEqualTo]: isOpEqualTo,
    [opMatches]: isOpMatches,
  }

  const operator = getOperatorFromQuery(operatorTest, query)

  function onOperatorChange(event) {
    if (event.target.value === opEqualTo && operator === opMatches) {
      onUpdateFilter(path, query.slice(1, -1))
    } else if (event.target.value === opMatches && operator === opEqualTo) {
      onUpdateFilter(path, `/${query}/`)
    } else {
      onUpdateFilter(path, '')
    }
  }

  return (
    <Grid columns={['150px', 'flex', 'auto']}>
      <Select options={operators} value={operator} onChange={onOperatorChange} />
      {
        operatorToWidget[operator]({path, query, schema, onUpdateFilter})
      }
    </Grid>
  )
}

const SearchWidgetBoolean = ({ path, query, onUpdateFilter }) => {
  return (
    <CheckBox value={query} onChange={(event) => onUpdateFilter(path, Boolean(event.target.checked))} />
  )
}

const SearchMetainfoFilters = ({ collection, filters, onFiltersChange }) => {
  const [schema, setSchema] = useState(undefined)

  useEffect(() => {
    getCollectionSchema(collection).then(
      result => setSchema(result)
    ).catch((error) => {
      setSchema(error)
    })
  }, [collection])

  const onUpdateFilter = (path, value) => {
    var filter = filters
    for (const key of path.slice(0, -1)) {
      filter = filter[key]
    }

    if (value !== undefined) {
      filter[path[path.length - 1]] = value
    } else if (Array.isArray(filter)) {
      filter.splice(path[path.length - 1], 1)
    } else {
      delete filter[path[path.length - 1]]
    }

    onFiltersChange(filters)
  }

  return (
    <FormField label='With filters...'>
      {
        renderState(schema, (schema) =>
          <SearchWidgetObjectKeys path={[]} query={filters || {}} schema={schema} onUpdateFilter={onUpdateFilter} />
        )
      }
    </FormField>
  )
}

export default SearchMetainfoFilters
