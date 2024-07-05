#!/usr/bin/python3

import os
import quart

from werkzeug.exceptions import HTTPException

from utils_security import load_rbac_configuration

API_ROOT='/api/'

APPLICATION_URL = os.environ.get('APPLICATION_URL', None)
CERTFILE = os.environ.get('CERTFILE', None)
KEYFILE = os.environ.get('KEYFILE', None)
RBACFILE = os.environ['RBACFILE']
SECRET_KEY = os.environ.get('SECRET_KEY', None)

load_rbac_configuration(RBACFILE)

app = quart.Quart(__name__, static_folder=None)

def load_module(app, modname):
  try:
    fullmodulename = 'mod_' + modname
    module = __import__(fullmodulename)
    app.register_blueprint(module.mod)
    print('Module {} loaded'.format(modname))
    return True
  except BaseException as ex:
    print('Module {} not loaded: {}'.format(modname, ex))
    return False

load_module(app, 'jenkins')
load_module(app, 'collections')
load_module(app, 'static')
load_module(app, 'openapi')

if not load_module(app, 'users_oauth2github'):
  load_module(app, 'users_none')

# Comment out to get stacktraces on console.
@app.errorhandler(Exception)
def handle_exception(exception):
  if isinstance(exception, HTTPException):
    return str(exception.description), exception.code
  return str(exception), 500

if __name__ == '__main__':
  if SECRET_KEY != None:
    app.secret_key = SECRET_KEY
    app.config['SESSION_TYPE'] = 'filesystem'
  if APPLICATION_URL != None:
    parts = APPLICATION_URL.split('://')[1].split(':')
    protocol = parts[0]
    host = parts[0]
    port = 443 if len(parts) == 1 else int(parts[1])
  else:
    host='0.0.0.0'
    port=8080
  app.run(host=host, port=port, certfile=CERTFILE, keyfile=KEYFILE)
