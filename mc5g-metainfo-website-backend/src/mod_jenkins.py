#!/usr/bin/python3

import motor
import motor.motor_asyncio
import os
import quart
import yaml

from ujenkins import JenkinsClient
from werkzeug.exceptions import NotFound, Conflict

from utils_security import ensure_role
from utils_collections import COLLECTION_MAPPING
from utils_collections import queryArtifact

API_ROOT='/api/'

MONGODB_URL = os.environ['MONGODB_URL']
MONGODB_COLLECTION = os.environ.get('MONGODB_COLLECTION', 'metainfo')

mongoClient = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
db = mongoClient[MONGODB_COLLECTION]

JENKINS_CONFIGURATION=None
with open(os.environ['JENKINSFILE'], 'r') as fp:
  JENKINS_CONFIGURATION = yaml.safe_load(fp)

mod = quart.Blueprint('jenkins', __name__)

@mod.route('{}solutions/<string:groupId>/<string:artifactId>/<string:version>/branch'.format(API_ROOT), methods = ['POST'])
async def branchArtifact(groupId, artifactId, version):
  col = COLLECTION_MAPPING['solutions']
  ensure_role(quart.session, quart.request, 'solution-branch')

  action_conf = JENKINS_CONFIGURATION['actions'].get('branch')
  if action_conf == None:
    raise Conflict("No branch action configured in application!")

  data = await queryArtifact(db, col, groupId, artifactId, version)
  if data == None:
    raise NotFound()
  if data['status'] != 'QA Ready':
    raise Conflict("Only solutions in QA Ready status can be branched.")

  parameters={
    'NF_TYPE': artifactId,
    'NF_VERSION': '-'.join(version.split('-')[:2]),
    'NEXT_STATUS': 'RC',
    'DRY_RUN': quart.request.args['dryRun'],
    'RC_VERSION': quart.request.args['rcVersion'],
  }

  # FIXME: Make asynchronous
  client=JenkinsClient(action_conf['server'], action_conf['username'], action_conf['password'], verify=False)
  client.builds.start(action_conf['job'], parameters=parameters)
  return quart.jsonify({})

@mod.route('{}products/<string:groupId>/<string:artifactId>/<string:version>/release'.format(API_ROOT), methods = ['POST'])
async def releaseArtifact(groupId, artifactId, version):
  col = COLLECTION_MAPPING['products']
  ensure_role(quart.session, quart.request, 'product-release')

  action_conf = JENKINS_CONFIGURATION['actions'].get('release')
  if action_conf == None:
    raise Conflict("No release action configured in application!")

  data = await queryArtifact(db, col, groupId, artifactId, version)
  if data == None:
    raise NotFound()
  if data['status'] != 'RC':
    raise Conflict("Only products in RC status can be released.")

  parameters={
    'PROD_METAINFO': artifactId,
    'VERSION': '-'.join(version.split('-')[:2]),
    'RELEASE': quart.request.args['release'],
    'DRAFT': quart.request.args['draft'],
    'DRY_RUN': quart.request.args['dryRun'],
  }

  # FIXME: Make asynchronous
  client=JenkinsClient(action_conf['server'], action_conf['username'], action_conf['password'], verify=False)
  client.builds.start(action_conf['job'], parameters=parameters)
  return quart.jsonify({})
