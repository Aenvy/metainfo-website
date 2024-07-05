#!/usr/bin/python3

import quart

from utils_security import get_roles_for_session

API_ROOT='/api/'
USER_ANONYMOUS = {
  'id': None,
  'name': 'Anonymous',
}

mod = quart.Blueprint('users_none', __name__)

@mod.route('{}users/self/roles'.format(API_ROOT), methods = ['GET'])
async def usersSelfRoles():
  return quart.jsonify(get_roles_for_session(quart.session, quart.request))

@mod.route('{}users/self'.format(API_ROOT), methods = ['GET'])
async def usersSelfProfile():
  return quart.jsonify(USER_ANONYMOUS)
