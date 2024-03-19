#!/usr/bin/python3

import yaml

from werkzeug.exceptions import Unauthorized

ROLES={
  'component-get',
  'component-list',
  'product-get',
  'product-list',
  'product-release',
  'quality-get',
  'quality-list',
  'result-get',
  'result-list',
  'solution-branch',
  'solution-get',
  'solution-list',
  'test-get',
  'test-list',
}

# Will be overwritten by load_rbac_configuration()
ANONYMOUS_ROLES=None
RBAC_POLICY=None

def _check_list_roles(policy, path):
  pathPolicy = policy
  for item in path.split('.'):
    pathPolicy = pathPolicy.get(item)

  unknown_roles = set(pathPolicy.keys()).difference(ROLES)

  if len(unknown_roles) > 0:
    raise RuntimeError('Unknown role(s) {} for profile {}'.format(','.join(unknown_roles), path))

def load_rbac_configuration(path):
  global RBAC_POLICY
  global ANONYMOUS_ROLES

  with open(path, 'r') as fp:
    policy = yaml.safe_load(fp)

  _check_list_roles(policy, 'anonymous')
  _check_list_roles(policy, 'authenticated')

  all_profiles = []
  for profile_type in ('groups', 'users', 'bearers'):
    for profile in policy.get(profile_type, {}):
      for profile_name in policy[profile_type].keys():
        all_profiles.append('{}.{}'.format(profile_type, profile_name))

  for profile in all_profiles:
    _check_list_roles(policy, profile)

  RBAC_POLICY=policy
  ANONYMOUS_ROLES = list(RBAC_POLICY['anonymous'].keys())
  ANONYMOUS_ROLES.sort()

def ensure_role(session, request, role):
  if not role in ROLES:
    raise RuntimeError('Unknown role {}'.format(role))

  client_roles = get_roles_for_session(session, request)
  if not role in client_roles:
    raise Unauthorized('Client does not have role {}'.format(role))

def get_roles_for_session(session, request):
  authorization = request.headers.get('Authorization')
  if authorization != None:
    authorization = authorization.split(' ')
    if len(authorization) == 2 and authorization[0].lower() == 'bearer':
      return list(RBAC_POLICY['bearers'].get(authorization[1], {}).keys())

  return session.get('roles', ANONYMOUS_ROLES)

def build_roles_for_session(user, groups):
  result = set(RBAC_POLICY['authenticated'].keys())
  for group in groups:
    result = result.union(set(RBAC_POLICY['groups'].get(group, {}).keys()))
  result = result.union(set(RBAC_POLICY['users'].get(user, {}).keys()))

  result = list(result)
  result.sort()
  return result
