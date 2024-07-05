import { metainfoApiUrl } from '../config'
import { toJsonOrError } from '../utils'

function toCompiledQuery(query) {
  const json = JSON.stringify(query)

  if (json !== '{}') {
    return json
  } else {
    return null
  }
}

// FIXME: Get valid statuses for collection from metainfo API.
export function statusesForCollection(collection) {
  return {
    'components': [
      'CT Ready',
      'CT Failed',
      'FT Ready',
      'FT Failed',
      'IT Ready',
      'IT Failed',
      'Val Ready',
      'Val Failed',
      'QA Ready',
      'QA Failed',
      'RC',
      'CA Released',
      'GA Released',
      'Blacklisted',
      'Deprecated',
      'Discontinued',
      'Discarded',
    ],
    'products': [
      'CT Ready',
      'CT Failed',
      'FT Ready',
      'FT Failed',
      'IT Ready',
      'IT Failed',
      'Val Ready',
      'Val Failed',
      'QA Ready',
      'QA Failed',
      'RC',
      'CA Released',
      'GA Released',
      'Blacklisted',
      'Deprecated',
      'Discontinued',
      'Discarded',
    ],
    'results': [
      'Passed',
      'Failed',
      'Discarded',
    ],
    'solutions': [
      'Val Ready',
      'Val Failed',
      'QA Ready',
      'QA Failed',
      'RC',
      'Archived',
      'Discarded',
    ],
  }[collection]
}

export function columnsPerCollection(collection) {
  return {
    'components': [
      'ident.groupId',
      'ident.artifactId',
      'ident.version',
      'status',
      'scm.branch',
      'tags',
    ],
    'products': [
      'ident.groupId',
      'ident.artifactId',
      'ident.version',
      'status',
      'scm.branch',
      'tags',
    ],
    'results': [
      'ident.groupId',
      'ident.artifactId',
      'ident.version',
      'status',
      'testType',
    ],
    'solutions': [
      'ident.groupId',
      'ident.artifactId',
      'ident.version',
      'status',
      'tags',
    ],
  }[collection]
}

function getListArtifactsUrl(collection, view, query, aggregateOn, start, count) {
  const compiledQuery = toCompiledQuery(query)

  const params = new URLSearchParams()
  if (view) {
    params.append('view', view)
  }
  if (compiledQuery) {
    params.append('query', compiledQuery)
  }
  if (aggregateOn) {
    if (aggregateOn.earliestFor) {
      params.append('earliestFor', aggregateOn.earliestFor.join(','))
    }
    if (aggregateOn.latestFor) {
      params.append('latestFor', aggregateOn.latestFor.join(','))
    }
  }
  if (start) {
    params.append('start', start)
  }
  if (count) {
    params.append('count', count)
  }

  const url = `${metainfoApiUrl}/${collection}?${params}`
  return url
}

export async function getListArtifacts(collection, view, query, aggregateOn, start, count) {
  const url = getListArtifactsUrl(collection, view, query, aggregateOn, start, count)
  const options = {
    headers: new Headers({
      'Accept': 'application/json'
    }),
    mode: 'cors'
  }
  const request = new Request(url, options)

  return fetch(request).then(response => toJsonOrError(response))
}

export async function downloadListArtifactsCsv(collection, view, query, aggregateOn, start, count, onDone) {
  const url = getListArtifactsUrl(collection, view, query, aggregateOn, start, count)
  const options = {
    headers: new Headers({
      'Accept': 'text/csv'
    }),
    mode: 'cors'
  }
  const request = new Request(url, options)

  fetch(request).then(response => {
    if (response.ok) {
      response.blob().then(data => {
        var a = document.createElement('a')
        a.href = window.URL.createObjectURL(data)
        a.download = 'metainfo-search-results.csv'
        a.dispatchEvent(new MouseEvent('click'))
        window.URL.revokeObjectURL(a.href)
        onDone()
      })
    } else {
      onDone()
    }
  })
}

export async function getArtifact(collection, artifactId, version) {
  const url = `${metainfoApiUrl}/${collection}/${artifactId}/${version}`
  const options = {
    headers: new Headers({
      'Accept': 'application/json'
    }),
    mode: 'cors'
  }
  const request = new Request(url, options)

  return fetch(request).then(response => toJsonOrError(response))
}

export async function getInventory(collection, artifactId, version) {
  const url = `${metainfoApiUrl}/${collection}/${artifactId}/${version}/inventory`;
  const options = {
    mode: 'cors'
  };
  const request = new Request(url, options);
  return fetch(request).then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.text(); // Return response text directly
  });
}

export async function getArtifactListArtifacts(collection, artifactId, version, subpath, view) {
  const params = new URLSearchParams()
  if (view) {
    params.append('view', view)
  }

  const url = `${metainfoApiUrl}/${collection}/${artifactId}/${version}/${subpath}?${params}`
  const options = {
    headers: new Headers({
      'Accept': 'application/json'
    }),
    mode: 'cors'
  }
  const request = new Request(url, options)

  return fetch(request).then(response => toJsonOrError(response))
}

export async function getCollectionSchema(collection) {
  const url = `${metainfoApiUrl}/${collection}/uiSchema`
  const options = {
    headers: new Headers({
      'Accept': 'application/json'
    }),
    mode: 'cors'
  }
  const request = new Request(url, options)

  return fetch(request).then(response => toJsonOrError(response))
}

export async function getListArtifactsFromIdents(collection, view, identifiers) {
  if (!Array.isArray(identifiers) || identifiers.length === 0) {
    return Promise.resolve({
      'count': 0,
      'members': []
    })
  }

  const compiledQuery = toCompiledQuery({ '$or': identifiers.map(ident => { return { 'ident': ident } }) })
  const params = new URLSearchParams()
  params.append('query', compiledQuery)
  if (view) {
    params.append('view', view)
  }

  const url = `${metainfoApiUrl}/${collection}?${params}`
  const options = {
    headers: new Headers({
      'Accept': 'application/json'
    }),
    mode: 'cors'
  }
  const request = new Request(url, options)

  return fetch(request).then(response => toJsonOrError(response))
}

export async function releaseArtifact(collection, artifactId, version, data) {
  const params = new URLSearchParams(data)

  const url = `${metainfoApiUrl}/${collection}/${artifactId}/${version}/release?${params}`
  const options = {
    method: 'POST',
    mode: 'cors',
  }
  const request = new Request(url, options)

  return fetch(request).then(response => toJsonOrError(response))
}

export async function branchArtifact(collection, artifactId, version, data) {
  const params = new URLSearchParams(data)

  const url = `${metainfoApiUrl}/${collection}/${artifactId}/${version}/branch?${params}`
  const options = {
    method: 'POST',
    mode: 'cors',
  }
  const request = new Request(url, options)

  return fetch(request).then(response => toJsonOrError(response))
}
