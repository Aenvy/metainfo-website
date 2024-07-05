#!/usr/bin/python3

import os
import quart

API_ROOT='/api/'

# FIXME: Ugly hack, need to properly package the backend...
from inspect import getsourcefile
OPENAPI_PATH=os.path.abspath(os.path.join(getsourcefile(lambda:0), os.pardir))

mod = quart.Blueprint('openapi', __name__)

@mod.route('{}swagger-ui'.format(API_ROOT), methods = ['GET'])
async def swaggerUi():
  return await quart.send_from_directory(OPENAPI_PATH, 'swagger-ui.html')

@mod.route('{}openapi.yaml'.format(API_ROOT), methods = ['GET'])
async def openapiYaml():
  return await quart.send_from_directory(OPENAPI_PATH, 'openapi.yaml')
