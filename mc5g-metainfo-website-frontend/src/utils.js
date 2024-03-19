import {
  Box,
  Spinner,
  Text
} from 'grommet'
import {
  CircleAlert,
  CircleInformation,
} from 'grommet-icons'

const uniqueArray = a => [...new Set(a.map(o => JSON.stringify(o)))].map(s => JSON.parse(s))

export function aggregateOn(items, fn) {
  return uniqueArray(items.members.map(fn).flat().filter(item => item != null).filter((value, index, self) => self.indexOf(value) === index))
}

export async function toJsonOrError(response) {
  if (response.ok) {
    return response.json()
  } else {
    if (response.statusText !== '') {
      throw new Error(`${response.statusText}: ${await response.text()}`)
    } else {
      throw new Error(`${await response.text()}`)
    }
  }
}

function defaultErrorFunc(data) {
  return (
    <Box direction='row' gap='small' margin='medium'>
      <CircleAlert color='red' />
      <Text>{data.message}</Text>
    </Box>
  )
}

function defaultDataFunc(data) {
  if (typeof data === 'string') {
    return (
      <Box direction='row' gap="small" margin='medium'>
        <CircleInformation color='blue' />
        <Text>{data}</Text>
      </Box>
    )
  } else {
    return data
  }
}

function defaultSpinnerFunc(data) {
  return (
    <Box>
      <Spinner
        alignSelf='center'
        message={{
          start: 'Loading...',
          end: 'Load complete.',
        }}
        margin='medium'
      />
    </Box>
  )
}

function defaultSpinnerIconFunc(data) {
  return (
    <Box>
      <Spinner
        alignSelf='center'
        message={{
          start: 'Loading...',
          end: 'Load complete.',
        }}
        margin={{
          top: 'xsmall',
          bottom: 'xsmall',
          left: 'small',
          right: 'small',
        }}
      />
    </Box>
  )
}

export function renderState(data, renderFn, errorFn, spinnerFn) {
  if (data instanceof Error) {
    return errorFn ? errorFn(data) : defaultErrorFunc(data)
  } else if (data !== undefined) {
    return renderFn ? renderFn(data) : defaultDataFunc(data)
  } else {
    return spinnerFn ? spinnerFn(data) : defaultSpinnerFunc(data)
  }
}

export function renderStateIcon(data, renderFn, errorFn, spinnerFn) {
  if (data instanceof Error) {
    return errorFn ? errorFn(data) : defaultErrorFunc(data)
  } else if (data !== undefined) {
    return renderFn ? renderFn(data) : defaultDataFunc(data)
  } else {
    return spinnerFn ? spinnerFn(data) : defaultSpinnerIconFunc(data)
  }
}

export function datumValue(datum, property) {
  if (!property) return undefined
  const parts = property.split('.')
  if (parts.length === 1) {
    return datum[property]
  }
  if (!datum[parts[0]]) {
    return undefined
  }
  return datumValue(datum[parts[0]], parts.slice(1).join('.'))
}

export function displayIfStatusFilter(statuses) {
  if (statuses.length > 0) {
    return item => statuses.includes(item.status)
  } else {
    return item => item.status !== 'Discarded'
  }
}

export function statusesFromSearchParams(value) {
  return (value || '').split(',').filter(i => i.length > 0)
}

export function statusesToSearchParams(value) {
  return value.filter(i => i.length > 0).join(',')
}

export const groupByToAggregateOn = {
  'branch': { 'latestFor': ['ident.groupId', 'ident.artifactId', 'scm.branch'] },
  'date': { 'latestFor': ['ident.groupId', 'ident.artifactId', 'ident.version:date'] },
  'version': { 'latestFor': ['ident.groupId', 'ident.artifactId', 'ident.version:version'] },
  'nothing': null,
}

function compareVersionPrivate(aVersion, bVersion) {
  const aVersionFields = aVersion.split(/\D/)
  const bVersionFields = bVersion.split(/\D/)
  const numCommonFields = Math.min(aVersionFields.length, bVersionFields.length)

  // Compare sequentially each group of digits as numbers.
  for (var index = 0; index < numCommonFields; index++) {
      const aField = parseInt(aVersionFields[index])
      const bField = parseInt(bVersionFields[index])

      if (aField !== bField) {
          const diff = aField - bField;

          if (diff < 0) {
              return -1
          } else if (diff > 0) {
              return 1
          } else {
              return 0
          }
      }
  }

  // Version with the most groups of digits wins.
  return aVersionFields.length - bVersionFields.length;
}

export function compareVersion(a, b) {
  const aVersion = a.ident.version
  const bVersion = b.ident.version

  const aVersionFields = aVersion.split('-')
  const bVersionFields = bVersion.split('-')
  const numCommonFields = Math.min(aVersionFields.length, bVersionFields.length)

  for (var index = 0; index < numCommonFields; index++) {
      const diff = compareVersionPrivate(aVersionFields[index], bVersionFields[index])

      if (diff !== 0) {
          return diff;
      }
  }

  // Version with the most groups of digits wins.
  return aVersionFields.length - bVersionFields.length
}

export function computeRelatedSearch(collection, groupId, artifactId, version, property) {
  return `/search?type=${collection}&filters=${JSON.stringify(computeRelatedFilters(groupId, artifactId, version, property))}`
}

export function computeRelatedFilters(groupId, artifactId, version, property) {
  return { [property]: { '$anyOf': [{ 'groupId': groupId, 'artifactId': artifactId, 'version': version }] } }
}
