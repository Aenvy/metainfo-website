import { metainfoApiUrl } from '../config'
import { toJsonOrError } from '../utils'

export const ROLE_COMPONENT_GET = 'component-get'
export const ROLE_COMPONENT_LIST = 'component-list'
export const ROLE_PRODUCT_GET = 'product-get'
export const ROLE_PRODUCT_LIST = 'product-list'
export const ROLE_PRODUCT_RELEASE = 'product-release'
export const ROLE_QUALITY_GET = 'quality-get'
export const ROLE_QUALITY_LIST = 'quality-list'
export const ROLE_RESULT_GET = 'result-get'
export const ROLE_RESULT_LIST = 'result-list'
export const ROLE_SOLUTION_BRANCH = 'solution-branch'
export const ROLE_SOLUTION_GET = 'solution-get'
export const ROLE_SOLUTION_LIST = 'solution-list'
export const ROLE_TEST_GET = 'test-get'
export const ROLE_TEST_LIST = 'test-list'

export async function getUserSelf() {
  if (sessionStorage.getItem('user')) {
    return Promise.resolve(JSON.parse(sessionStorage.getItem('user')))
  }

  const url = `${metainfoApiUrl}/users/self`
  const options = {
    headers: new Headers({
      'Accept': 'application/json'
    }),
    mode: 'cors'
  }
  const request = new Request(url, options)

  return fetch(request).then(response => toJsonOrError(response).then(json => {
      sessionStorage.setItem('user', JSON.stringify(json))
      return getUserSelf()
    }
  ))
}

export async function getUserSelfRoles() {
  if (sessionStorage.getItem('roles')) {
    return Promise.resolve(JSON.parse(sessionStorage.getItem('roles')))
  }

  const url = `${metainfoApiUrl}/users/self/roles`
  const options = {
    headers: new Headers({
      'Accept': 'application/json'
    }),
    mode: 'cors'
  }
  const request = new Request(url, options)

  return fetch(request).then(response => toJsonOrError(response).then(json => {
      sessionStorage.setItem('roles', JSON.stringify(json))
      return getUserSelfRoles()
    }
  ))
}

function resetSession() {
  sessionStorage.removeItem('user')
  sessionStorage.removeItem('roles')
}

export function login() {
  resetSession()

  const params = new URLSearchParams()
  params.append('redirect', window.location)

  window.location = `${metainfoApiUrl}/login/oauth2?${params}`
}

export function logout() {
  const url = `${metainfoApiUrl}/logout`
  const options = {
    method: 'POST',
    mode: 'cors',
  }
  const request = new Request(url, options)

  fetch(request).then(response => {
    if (response.ok) {
      resetSession()

      // Force a refresh of the webpage.
      // eslint-disable-next-line
      window.location = window.location
    }
  })
}
