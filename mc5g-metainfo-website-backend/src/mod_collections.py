#!/usr/bin/python3

import json
import motor
import motor.motor_asyncio
import os
import quart
import re
import yaml
import requests

from werkzeug.exceptions import BadRequest, NotFound

from schema2json import schema2json
from query import Query

from utils_collections import *
from utils_security import ensure_role
from module_utils.status import Status, min_status

API_ROOT='/api/'

MONGODB_URL = os.environ['MONGODB_URL']
MONGODB_COLLECTION = os.environ.get('MONGODB_COLLECTION', 'metainfo')

mongoClient = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
db = mongoClient[MONGODB_COLLECTION]

def get_groupId(collection):
    if collection == COLLECTION_MAPPING['solutions']:
      return f'com.hpe.cms.5g.{collection}'
    else:
      return f'com.hpe.cms.5g.{collection}.*'

mod = quart.Blueprint('collections', __name__)

collection = COLLECTION_MAPPING['solutions']
rc = r'<rc:re:\d\.\d{4}\.\d-.*>'
async def _tagged_metainfo(collection, tag="", rc=True):
    
    if tag.startswith("MC5G-"):
        tag = tag[5:]
    query = {'$or': [{'tags': {'$regex': tag}}, {'ident.branch': {'$regex': tag}}]} \
        if tag else {'tags': {'$nin': [None, [], ""]}}
    query['status'] = {'$nin': min_status('RC')}
    if not rc:
        query['status']['$nin'].append('RC')
    cursor = db[collection].find(query)
    return await cursor.to_list(length=None)

@mod.route("{}releases".format(API_ROOT), methods = ['GET'])

@mod.route("{}releases/<string:tag>".format(API_ROOT), methods = ['GET'])
async def get_releases_endpoint(tag=""):
    rc_param = quart.request.args.get('rc', False)
    # Ensure that 'db' object is initialized and imported correctly
    rcsol = await _tagged_metainfo("sol", tag=tag, rc=True)
    prods = {
        f"{p['artifactId']}/{p['version']['base']}": p
        for p in await _tagged_metainfo("prod", tag=tag, rc=rc_param)
    }
    r = {
        f"{sol['name']} [{tag.replace('MC5G-', '')}]": {
            'version': sol['version']['base'],
            'artifactId': sol['artifactId'],
            'metainfo': sol,
            'products': {
                f"{prod['name']} [{tag.replace('MC5G-', '')}]": {
                    'version': prod['version']['base'],
                    'artifactId': prod['artifactId'],
                    'metainfo': prod,
                }
                for pident, prod in prods.items()
                if pident in prodident
                and tag in prod['tags']
            }
        }
        for sol in rcsol
        for tag in sol['tags']
        for prodident in [{
            f"{p['groupId']}/{p['artifactId']}/{p['version']['base']}"
            for p in sol['products']
        }]
    }
    return {k: v for k, v in r.items() if v['products']}

@mod.route('{}<string:collection>/uiSchema'.format(API_ROOT), methods = ['GET'])
async def getCollectionSchema(collection):
  schema = COLLECTION_TO_SCHEMA[collection]
  role = COLLECTION_TO_ROLE_LIST[collection]
  ensure_role(quart.session, quart.request, role)

  return quart.jsonify(schema2json(schema))

@mod.route('{}<string:collection>/<string:artifactId>/<string:version>'.format(API_ROOT), methods = ['GET'])
async def getArtifact(collection, artifactId, version):
  schema = COLLECTION_TO_SCHEMA[collection]
  col = COLLECTION_MAPPING[collection]
  groupId = get_groupId(col)
  role = COLLECTION_TO_ROLE_GET[collection]
  ensure_role(quart.session, quart.request, role)
  if collection == COLLECTION_MAPPING['solutions']:
    data = await queryArtifact(db, collection, groupId, artifactId, version, view=quart.request.args.get('view', 'full'))
  else:
    data = await querySubArtifact(db, collection, artifactId, version, view=quart.request.args.get('view', 'full'))
  if data != None:
    if not quart.request.args.get('raw', 'false') == 'true':
      data = migrateMetainfo(schema, data)
    return quart.jsonify(data)
  else:
    raise NotFound()

@mod.route('{}<string:collection>/<string:artifactId>/<string:version>/graph'.format(API_ROOT), methods = ['GET'])
async def getArtifactGraph(collection, artifactId, version):
  schema = COLLECTION_TO_SCHEMA[collection]
  col = COLLECTION_MAPPING[collection]
  groupId = get_groupId(col)
  role = COLLECTION_TO_ROLE_GET[collection]
  ensure_role(quart.session, quart.request, role)

  result = await queryArtifactGraph(db, collection, groupId, artifactId, version)

  if result != None:
    return graphResponse(result, quart.request.accept_mimetypes)
  else:
    raise NotFound()

@mod.route('{}<string:collection>/watch'.format(API_ROOT), methods = ['GET'])
async def watchListArtifacts(collection):
  role = COLLECTION_TO_ROLE_LIST[collection]
  ensure_role(quart.session, quart.request, role)

  @quart.helpers.stream_with_context
  async def metainfo_stream():
    params_subset = {k:v for k,v in quart.request.args.items() if k in {'view', 'query', 'latestFor', 'raw'}}
    parsed_args = buildSearchFromArgs(db, collection, params_subset)

    async for timestamp, event, data in watchArtifacts(db, collection, view=parsed_args['view'], query=parsed_args['query'], watchQuery=parsed_args['watchQuery'], latestFor=parsed_args['latestFor'], raw=parsed_args['raw']):
      yield f"timestamp: {timestamp}\r\nevent: {event}\r\ndata: {json.dumps(data)}\r\n\r\n"

  response = await quart.make_response(metainfo_stream())
  response.mimetype = 'text/event-stream'
  response.timeout = None
  return response

@mod.route('{}<string:collection>'.format(API_ROOT), methods = ['GET'])
async def getListArtifacts(collection):
  role = COLLECTION_TO_ROLE_LIST[collection]
  ensure_role(quart.session, quart.request, role)

  result = await searchArtifacts(**buildSearchFromArgs(db, collection, quart.request.args))

  return collectionResponse(result, quart.request.accept_mimetypes)

@mod.route('{}components/<string:artifactId>/<string:version>/buildDependencies'.format(API_ROOT), methods = ['GET'])
async def getComponentBuildDependencies(artifactId, version):
  role = COLLECTION_TO_ROLE_GET['components']
  ensure_role(quart.session, quart.request, role)

  component = await querySubArtifact(db, 'components', artifactId, version)
  if component == None:
    raise NotFound()

  query = identToQuery(component, ['deps', 'build'])
  if query == None:
    result = searchEmpty('components')
  else:
    result = await searchArtifacts(**buildSearchFromArgs(db, 'components', quart.request.args, query=query))

  return collectionResponse(result, quart.request.accept_mimetypes)

@mod.route('{}components/<string:artifactId>/<string:version>/runtimeDependencies'.format(API_ROOT), methods = ['GET'])
async def getComponentRuntimeDependencies(artifactId, version):
  role = COLLECTION_TO_ROLE_GET['components']
  ensure_role(quart.session, quart.request, role)

  component = await querySubArtifact(db, 'components', artifactId, version)
  if component == None:
    raise NotFound()

  query = identToQuery(component, ['deps', 'runtime'])
  if query == None:
    result = searchEmpty('components')
  else:
    result = await searchArtifacts(**buildSearchFromArgs(db, 'components', quart.request.args, query=query))

  return collectionResponse(result, quart.request.accept_mimetypes)

@mod.route('{}products/<string:artifactId>/<string:version>/components'.format(API_ROOT), methods = ['GET'])
async def getProductComponents(artifactId, version):
  role = COLLECTION_TO_ROLE_GET['products']
  ensure_role(quart.session, quart.request, role)

  product = await querySubArtifact(db, 'products', artifactId, version)
  if product == None:
    raise NotFound()

  query = identToQuery(product, ['components'])
  if query == None:
    result = searchEmpty('components')
  else:
    result = await searchArtifacts(**buildSearchFromArgs(db, 'components', quart.request.args, query=query))

  return collectionResponse(result, quart.request.accept_mimetypes)

@mod.route('{}products/<string:artifactId>/<string:version>/components/buildDependencies'.format(API_ROOT), methods = ['GET'])
async def getProductComponentsBuildDependencies(artifactId, version):
  role = COLLECTION_TO_ROLE_GET['products']

  ensure_role(quart.session, quart.request, role)

  product = await querySubArtifact(db, 'products', artifactId, version)
  if product == None:
    raise NotFound()
  query = identToQuery(product, ['components'])
  if query == None:
    result = searchEmpty('components')
  else:
    result = await searchArtifacts(**buildSearch(db, 'components', query=query))
    query = identToQuery(result['members'], ['deps', 'build'])
    if query == None:
      result = searchEmpty('components')
    else:
      result = await searchArtifacts(**buildSearchFromArgs(db, 'components', quart.request.args, query=query))

  return collectionResponse(result, quart.request.accept_mimetypes)

@mod.route('{}products/<string:artifactId>/<string:version>/components/runtimeDependencies'.format(API_ROOT), methods = ['GET'])
async def getProductComponentsRuntimeDependencies(artifactId, version):
  role = COLLECTION_TO_ROLE_GET['products']

  ensure_role(quart.session, quart.request, role)

  product = await querySubArtifact(db, 'products', artifactId, version)
  if product == None:
    raise NotFound()

  query = identToQuery(product, ['components'])
  if query == None:
    result = searchEmpty('components')
  else:
    result = await searchArtifacts(**buildSearch(db, 'components', query=query))
    query = identToQuery(result['members'], ['deps', 'runtime'])
    if query == None:
      result = searchEmpty('components')
    else:
      result = await searchArtifacts(**buildSearchFromArgs(db, 'components', quart.request.args, query=query))

  return collectionResponse(result, quart.request.accept_mimetypes)

@mod.route('{}solutions/<string:artifactId>/<string:version>/products'.format(API_ROOT), methods = ['GET'])
async def getSolutionProducts(artifactId, version):
  role = COLLECTION_TO_ROLE_GET['solutions']
  col = COLLECTION_MAPPING['solutions']
  groupId = get_groupId(col)
  ensure_role(quart.session, quart.request, role)

  solution = await queryArtifact(db, 'solutions', groupId, artifactId, version)
  if solution == None:
    raise NotFound()

  query = identToQuery(solution, ['products'])
  if query == None:
    result = searchEmpty('products')
  else:
    result = await searchArtifacts(**buildSearchFromArgs(db, 'products', quart.request.args, query=query))

  return collectionResponse(result, quart.request.accept_mimetypes)

@mod.route('{}solutions/<string:artifactId>/<string:version>/products/components'.format(API_ROOT), methods = ['GET'])
async def getSolutionProductsComponents(artifactId, version):
  role = COLLECTION_TO_ROLE_GET['solutions']
  col = COLLECTION_MAPPING['solutions']
  groupId = get_groupId(col)
  ensure_role(quart.session, quart.request, role)

  solution = await queryArtifact(db, 'solutions', groupId, artifactId, version)
  if solution == None:
    raise NotFound()

  query = identToQuery(solution, ['products'])
  if query == None:
    result = searchEmpty('products')
  else:
    result = await searchArtifacts(**buildSearch(db, 'products', query=query))
    query = identToQuery(result['members'], ['components'])
    if query == None:
      result = searchEmpty('components')
    else:
      result = await searchArtifacts(**buildSearchFromArgs(db, 'components', quart.request.args, query=query))

  return collectionResponse(result, quart.request.accept_mimetypes)

@mod.route('{}solutions/<string:artifactId>/<string:version>/products/components/buildDependencies'.format(API_ROOT), methods = ['GET'])
async def getSolutionProductsComponentsBuildDependencies(artifactId, version):
  role = COLLECTION_TO_ROLE_GET['solutions']
  col = COLLECTION_MAPPING['solutions']
  groupId = get_groupId(col)
  ensure_role(quart.session, quart.request, role)

  solution = await queryArtifact(db, 'solutions', groupId, artifactId, version)
  if solution == None:
    raise NotFound()

  query = identToQuery(solution, ['products'])
  if query == None:
    result = searchEmpty('products')
  else:
    result = await searchArtifacts(**buildSearch(db, 'products', query=query))
    query = identToQuery(result['members'], ['components'])
    if query == None:
      result = searchEmpty('components')
    else:
      result = await searchArtifacts(**buildSearch(db, 'components', query=query))
      query = identToQuery(result['members'], ['deps', 'build'])
      if query == None:
        result = searchEmpty('components')
      else:
        result = await searchArtifacts(**buildSearchFromArgs(db, 'components', quart.request.args, query=query))

  return collectionResponse(result, quart.request.accept_mimetypes)

@mod.route('{}solutions/<string:artifactId>/<string:version>/products/components/runtimeDependencies'.format(API_ROOT), methods = ['GET'])
async def getSolutionProductsComponentsRuntimeDependencies(artifactId, version):
  role = COLLECTION_TO_ROLE_GET['solutions']
  col = COLLECTION_MAPPING['solutions']
  groupId = get_groupId(col)
  ensure_role(quart.session, quart.request, role)

  solution = await queryArtifact(db, 'solutions', groupId, artifactId, version)
  if solution == None:
    raise NotFound()

  query = identToQuery(solution, ['products'])
  if query == None:
    result = searchEmpty('products')
  else:
    result = await searchArtifacts(**buildSearch(db, 'products', query=query))
    query = identToQuery(result['members'], ['components'])
    if query == None:
      result = searchEmpty('components')
    else:
      result = await searchArtifacts(**buildSearch(db, 'components', query=query))
      query = identToQuery(result['members'], ['deps', 'runtime'])
      if query == None:
        result = searchEmpty('components')
      else:
        result = await searchArtifacts(**buildSearchFromArgs(db, 'components', quart.request.args, query=query))

  return collectionResponse(result, quart.request.accept_mimetypes)

@mod.route('{}solutions/<string:artifactId>/<string:version>/inventory'.format(API_ROOT), methods = ['GET'])
async def getInventoryContent(artifactId, version):
  role = COLLECTION_TO_ROLE_GET['results']
  col = COLLECTION_MAPPING['solutions']
  groupId = get_groupId(col)
  ensure_role(quart.session, quart.request, role)
  version_list = [version, re.sub(r'-\d{1,2}$', '', version)]

  for ver in version_list:
    try:
      result = await queryResultArtifact(db, 'results', groupId, artifactId, ver)
      if result:
        inventory_url = result.get('inventory', None)
        if inventory_url:
          response = requests.get(inventory_url, verify=False)
          if response.status_code == 200:
            content_type = response.headers.get('Content-Type', '')
            return quart.Response(status=200, response=response.text, content_type=content_type)
          else:
            return quart.Response(status=response.status_code, text="Failed to fetch inventory content")
        else:
          return "Inventory URL not found for the specified document."
      else:
        raise NotFound()
    except NotFound:
      continue

  # If none of the versions return data, raise NotFound
  raise NotFound()
