#!/usr/bin/python3

import os
import quart
import random
import requests

from oauthlib.oauth2 import WebApplicationClient

from utils_security import get_roles_for_session, build_roles_for_session

API_ROOT='/api/v2/'
OAUTH2_SCOPES=['read:user', 'read:org']
USER_ANONYMOUS={
  'id': None,
  'name': 'Anonymous',
}
USER_ANONYMOUS_TEAMS=[]

APPLICATION_URL = os.environ['APPLICATION_URL']
GITHUB_API_URL = os.environ['GITHUB_API_URL']
OAUTH2_LOGIN_URL = os.environ['OAUTH2_LOGIN_URL']
OAUTH2_CLIENT_ID = os.environ['OAUTH2_CLIENT_ID']
OAUTH2_CLIENT_SECRET = os.environ['OAUTH2_CLIENT_SECRET']

OAUTH2_REDIRECT_URL = '{}{}login/oauth2callback'.format(APPLICATION_URL, API_ROOT)

mod = quart.Blueprint('users_oauth2github', __name__)

def _getTeamsResponse(token):
  header = {
    'Accept': 'application/vnd.github+json',
    'Authorization': '{} {}'.format(token['token_type'], token['access_token'])
  }
  # FIXME: Make asynchronous
  return requests.get('{}/user/teams?per_page=100'.format(GITHUB_API_URL), headers=header)

def _getUserSelfResponse(token):
  header = {
    'Accept': 'application/vnd.github+json',
    'Authorization': '{} {}'.format(token['token_type'], token['access_token'])
  }
  # FIXME: Make asynchronous
  return requests.get('{}/user'.format(GITHUB_API_URL), headers=header)

@mod.route('{}login/oauth2'.format(API_ROOT), methods = ['GET'])
async def login():
  client = WebApplicationClient(OAUTH2_CLIENT_ID)

  quart.session['oauth2.state'] = f'{random.getrandbits(64):016x}'
  quart.session['oauth2.redirect'] = quart.request.args['redirect']

  url = client.prepare_request_uri(
    '{}/authorize'.format(OAUTH2_LOGIN_URL),
    redirect_uri = OAUTH2_REDIRECT_URL,
    scope = OAUTH2_SCOPES,
    state = quart.session['oauth2.state'],
  )

  return quart.redirect(url)

@mod.route('{}login/oauth2callback'.format(API_ROOT), methods = ['GET'])
async def loginRedirect():
  code = quart.request.args['code']
  state = quart.request.args['state']
  if state != quart.session.get('oauth2.state', None):
    return 'OAuth2 state information mismatch', 401
  else:
    del quart.session['oauth2.state']

  redirect = quart.session['oauth2.redirect']
  del quart.session['oauth2.redirect']

  client = WebApplicationClient(OAUTH2_CLIENT_ID)
  data = client.prepare_request_body(
    code = code,
    redirect_uri = OAUTH2_REDIRECT_URL,
    client_id = OAUTH2_CLIENT_ID,
    client_secret = OAUTH2_CLIENT_SECRET,
  )

  # FIXME: Make asynchronous
  response = requests.post('{}/access_token'.format(OAUTH2_LOGIN_URL), data=data)
  response.raise_for_status()
  client.parse_request_body_response(response.text)

  user = _getUserSelfResponse(client.token)
  user.raise_for_status()
  teams = _getTeamsResponse(client.token)
  teams.raise_for_status()

  quart.session['roles'] = build_roles_for_session(user.json()['login'], [team['slug'] for team in teams.json()])
  quart.session['oauth2.token'] = client.token

  return quart.redirect(redirect)

@mod.route('{}logout'.format(API_ROOT), methods = ['POST'])
async def logout():
  quart.session.clear()
  return quart.jsonify({})

@mod.route('{}users/self/teams'.format(API_ROOT), methods = ['GET'])
async def usersSelfTeams():
  token = quart.session.get('oauth2.token', None)

  if token != None:
    response = _getTeamsResponse(token)
    return quart.jsonify(response.json()), response.status_code
  else:
    return quart.jsonify(USER_ANONYMOUS_TEAMS)

@mod.route('{}users/self/roles'.format(API_ROOT), methods = ['GET'])
async def usersSelfRoles():
  return quart.jsonify(get_roles_for_session(quart.session, quart.request))

@mod.route('{}users/self'.format(API_ROOT), methods = ['GET'])
async def usersSelfProfile():
  token = quart.session.get('oauth2.token', None)

  if token != None:
    response = _getUserSelfResponse(token)
    return quart.jsonify(response.json()), response.status_code
  else:
    return quart.jsonify(USER_ANONYMOUS)
