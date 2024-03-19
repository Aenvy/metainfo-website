#!/usr/bin/python3

import csv
import io
import json
import os
import quart

from werkzeug.exceptions import BadRequest

from collections import defaultdict
from datetime import datetime
from functools import partial
from itertools import chain, islice
from operator import is_not

from module_utils.schema.definitions import deliverable

from module_utils.schema.caasschema import CaasSchema
from module_utils.schema.componentschema import ComponentSchema
from module_utils.schema.productschema import ProductSchema
from module_utils.schema.qualityschema import QualitySchema
from module_utils.schema.resultschema import ResultSchema
from module_utils.schema.solutionschema import SolutionSchema
from module_utils.schema.testschema import TestSchema

from aggregate import earliestMetainfosFor, latestMetainfosFor, sortMetainfosBy
from query import Query

COLLECTION_MAPPING={
  'caas': 'caas',
  'products': 'prod',
  'components': 'comp',
  'quality': 'quality',
  'results': 'result',
  'solutions': 'sol',
  'tests': 'test',
}

COLLECTION_TO_SCHEMA={
  'caas': CaasSchema,
  'products': ProductSchema,
  'components': ComponentSchema,
  'quality': QualitySchema,
  'results': ResultSchema,
  'solutions': SolutionSchema,
  'tests': TestSchema,
}

COLLECTION_TO_ROLE_LIST={
  'caas': 'caas-list',
  'products': 'product-list',
  'components': 'component-list',
  'quality': 'quality-list',
  'results': 'result-list',
  'solutions': 'solution-list',
  'tests': 'test-list',
}

COLLECTION_TO_ROLE_GET={
  'caas': 'caas-get',
  'products': 'product-get',
  'components': 'component-get',
  'quality': 'quality-get',
  'results': 'result-get',
  'solutions': 'solution-get',
  'tests': 'test-get',
}

VIEW_TO_PROJECTION={
  'full': {'_id': False},
  'condense': {'schema': True, 'ident': True, '_id': False},
  'summary': {'schema': True, 'ident': True, 'name': True, 'description': True, 'scm': True, 'status': True, 'tags': True, 'testType': True, 'products': True, 'components': True, 'deps': True, '_id': False},
}

VIEW_TO_WATCH_PROJECTION={
  'condense': {
    '_id': True,
    'operationType': True,
    'fullDocument.schema': True,
    'fullDocument.ident': True,
  },
  'summary': {
    '_id': True,
    'operationType': True,
    'fullDocument.schema': True,
    'fullDocument.ident': True,
    'fullDocument.name': True,
    'fullDocument.description': True,
    'fullDocument.scm': True,
    'fullDocument.status': True,
    'fullDocument.tags': True,
    'fullDocument.testType': True,
    'fullDocument.products': True,
    'fullDocument.components': True,
    'fullDocument.deps': True,
  },
}

METAINFO_MIGRATION_HISTORY_JENKINS_BASE_URL=os.environ.get('METAINFO_MIGRATION_HISTORY_JENKINS_BASE_URL', False)
METAINFO_MIGRATION_HISTORY_JENKINS_BASE_URL_NHSS=os.environ.get('METAINFO_MIGRATION_HISTORY_JENKINS_BASE_URL_NHSS', False)

def queryArtifact(database, collection, groupId, artifactId, version, view='full'):
  col = COLLECTION_MAPPING[collection]
  filter = {'ident.groupId': groupId, 'ident.artifactId': artifactId, 'ident.version': version}
  projection = VIEW_TO_PROJECTION[view]

  return database[col].find_one(filter=filter, projection=projection)

def queryResultArtifact(database, collection, groupId, artifactId, version, view='full'):
  col = COLLECTION_MAPPING[collection]
  filter = {'identifiers.groupId': groupId, 'identifiers.artifactId': artifactId, 'identifiers.version': version}
  projection = VIEW_TO_PROJECTION[view]

  return database[col].find_one(filter=filter, projection=projection)

async def queryArtifactGraph(database, collection, groupId, artifactId, version):
  col = COLLECTION_MAPPING[collection]
  projection = VIEW_TO_PROJECTION['summary']

  def buildNodeId(collection, groupId, artifactId, version):
    return f"{collection}/{groupId}/{artifactId}/{version}"
  def buildNodeIdFromArtifact(collection, artifact):
    return buildNodeId(collection, artifact['ident']['groupId'], artifact['ident']['artifactId'], artifact['ident']['version'])

  async def processArtifact(collection, artifact, artifacts, links):
    artifactId = buildNodeIdFromArtifact(collection, artifact)
    if artifactId in artifacts:
      return

    artifacts[artifactId] = artifact
    artifactType = artifact['schema'].split('/')[1]

    awaitables = []
    if artifactType == 'solution.schema.json':
      query = identToQuery(artifact, ['products'])
      if query != None:
        result = await searchArtifacts(**buildSearch(database, 'products', query=query, view='summary'))
        for item in result['members']:
          links.add((artifactId, 'product', buildNodeIdFromArtifact('products', item)))
          awaitables.append(processArtifact('products', item, artifacts, links))
    elif artifactType == 'product.schema.json':
      query = identToQuery(artifact, ['components'])
      if query != None:
        result = await searchArtifacts(**buildSearch(database, 'components', query=query, view='summary'))
        for item in result['members']:
          links.add((artifactId, 'component', buildNodeIdFromArtifact('components', item)))
          awaitables.append(processArtifact('components', item, artifacts, links))
    elif artifactType == 'component.schema.json':
      query = identToQuery(artifact, ['deps', 'build'])
      if query != None:
        result = await searchArtifacts(**buildSearch(database, 'components', query=query, view='summary'))
        for item in result['members']:
          links.add((artifactId, 'buildDependency', buildNodeIdFromArtifact('components', item)))
          awaitables.append(processArtifact('components', item, artifacts, links))
      query = identToQuery(artifact, ['deps', 'runtime'])
      if query != None:
        result = await searchArtifacts(**buildSearch(database, 'components', query=query, view='summary'))
        for item in result['members']:
          links.add((artifactId, 'runtimeDependency', buildNodeIdFromArtifact('components', item)))
          awaitables.append(processArtifact('components', item, artifacts, links))
    for awaitable in awaitables:
      await awaitable

  artifacts = dict()
  links = set()

  artifact = await queryArtifact(database, collection, groupId, artifactId, version, view='summary')

  if artifact != None:
    await processArtifact(collection, artifact, artifacts, links)
    return {
      'nodes': artifacts,
      'links': tuple({'source': link[0], 'type': link[1], 'target': link[2]} for link in links),
    }
  return None

def buildSearch(db, collection, start=0, count=2**16, view='full', query={}, earliestFor=None, latestFor=None, sortBy=None, raw=False):
  schema = COLLECTION_TO_SCHEMA[collection]

  try:
    compiledQuery = Query(schema, query).getCompiledQuery()
    compiledWatchQuery = Query(schema, query).getCompiledQuery(['fullDocument'])
  except RuntimeError as err:
    raise BadRequest('Failed to compile query: {}'.format(str(err)))

  return {
    'db': db,
    'collection': collection,
    'start': start,
    'count': count,
    'view': view,
    'query': compiledQuery,
    'watchQuery': compiledWatchQuery,
    'earliestFor': earliestFor,
    'latestFor': latestFor,
    'sortBy': sortBy,
    'raw': raw
  }

def buildSearchFromArgs(db, collection, args, start=None, count=None, view=None, query=None, earliestFor=None, latestFor=None, sortBy=None, raw=None):
  if start == None:
    try:
      start = int(args.get('start', 0))
    except ValueError as err:
      raise BadRequest('Invalid value for start: {}'.format(str(err)))
  if count == None:
    try:
      count = int(args.get('count', 2 ** 16))
    except ValueError as err:
      raise BadRequest('Invalid value for count: {}'.format(str(err)))

  if query == None:
    try:
      query = json.loads(args.get('query', '{}'))
    except json.decoder.JSONDecodeError as err:
      raise BadRequest('Failed to parse query: {}'.format(str(err)))

  if earliestFor == None:
    try:
      earliestFor = args.get('earliestFor', None)
      if earliestFor != None:
        earliestFor = earliestFor.split(',')
    except BaseException as err:
      raise BadRequest('Failed to parse earliestFor: {}'.format(str(err)))

  if latestFor == None:
    try:
      latestFor = args.get('latestFor', None)
      if latestFor != None:
        latestFor = latestFor.split(',')
    except BaseException as err:
      raise BadRequest('Failed to parse latestFor: {}'.format(str(err)))

  if earliestFor != None and latestFor != None:
    raise BadRequest('At most one of earliestFor and latestFor can be used')

  if sortBy == None:
    try:
      sortBy = args.get('sortBy', None)
      if sortBy != None:
        sortBy = sortBy.split(',')
    except BaseException as err:
      raise BadRequest('Failed to parse sortBy: {}'.format(str(err)))

  if view == None:
    view = args.get('view', 'full')

  if raw == None:
    raw = args.get('raw', 'false') == 'true'

  return buildSearch(
    db=db,
    collection=collection,
    start=start,
    count=count,
    view=view,
    query=query,
    earliestFor=earliestFor,
    latestFor=latestFor,
    sortBy=sortBy,
    raw=raw
  )

async def watchArtifacts(db, collection, view='full', query={}, watchQuery={}, latestFor=None, raw=False):
  col = COLLECTION_MAPPING[collection]
  schema = COLLECTION_TO_SCHEMA[collection]

  if latestFor != None:
    metainfos = list((await searchArtifacts(db, collection, view=view, query=query, latestFor=latestFor, raw=raw))['members'])
    yield (datetime.now().isoformat(), 'context', metainfos)

  pipeline = [{'$match': watchQuery}]
  if view in VIEW_TO_WATCH_PROJECTION:
    pipeline.append({'$project': VIEW_TO_WATCH_PROJECTION[view]})

  async with db[col].watch(pipeline=pipeline) as change_stream:
    async for change in change_stream:
      if change['operationType'] == 'insert':
        # FIXME: Hack to remove _id from watch document.
        metainfo = {x: change['fullDocument'][x] for x in change['fullDocument'] if x not in {'_id'}}
        if not raw == True:
          metainfo = migrateMetainfo(schema, metainfo)
        if latestFor == None:
          yield (datetime.now().isoformat(), 'insert', metainfo)
        else:
          # FIXME: Hackish way to maintain a metainfo set.
          new_metainfos = latestMetainfosFor(metainfos + [metainfo], latestFor)
          new_metainfos = sortMetainfosBy(new_metainfos, ['ident.groupId', 'ident.artifactId', 'ident.version'])
          if len(new_metainfos) > len(metainfos):
            metainfos = new_metainfos
            yield (datetime.now().isoformat(), 'new', metainfo)
          # FIXME: Hackish way to deep compare metainfo sets.
          elif json.dumps(new_metainfos, sort_keys=True) != json.dumps(metainfos, sort_keys=True):
            metainfos = new_metainfos
            yield (datetime.now().isoformat(), 'newer', metainfo)

# FIXME: Remove unused watchQuery parameter.
async def searchArtifacts(db, collection, start=0, count=2**16, view='full', query={}, watchQuery=None, earliestFor=None, latestFor=None, sortBy=None, raw=False):
  col = COLLECTION_MAPPING[collection]
  schema = COLLECTION_TO_SCHEMA[collection]

  projection = VIEW_TO_PROJECTION[view]

  if earliestFor == None and latestFor == None:
    limit = count
  else:
    limit = 2 ** 31

  awaitable_members = db[col].find(filter=query, projection=projection, skip=start, limit=limit).to_list(length=None)
  awaitable_total = db[col].count_documents(query)

  # FIXME: use asyncio.get_running_loop() and wrap CPU-bound stuff inside loop.run_in_executor()
  #        once we get rid of Python 3.6 in production

  result_members = await awaitable_members

  if earliestFor != None:
    result_members = islice(earliestMetainfosFor(result_members, earliestFor), count)
  elif latestFor != None:
    result_members = islice(latestMetainfosFor(result_members, latestFor), count)

  if sortBy != None:
    result_members = sortMetainfosBy(result_members, sortBy)

  if view == 'full' and not raw == True:
    def _migrate(metainfo, schema=schema):
      return migrateMetainfo(schema, metainfo)
    result_members = map(_migrate, result_members)

  result_members = tuple(result_members)
  result_total = await awaitable_total

  return {
    'name': collection,
    'count': len(result_members),
    'members': result_members,
    'total': result_total,
    'debug': {
      'filter': str(query),
    }
  }

def searchEmpty(collection):
  return {
    'name': collection,
    'count': 0,
    'members': [],
    'total': 0
  }

def isolateIdents(data, path):
  def sanitize(ident):
    return {
      'groupId': ident['groupId'],
      'artifactId': ident['artifactId'],
      'version': ident['version']
    }
  def crawl(x, path=path):
    for item in path:
      x = x.get(item, None)
      if x == None:
        return []
    if isinstance(x, dict):
      return sanitize(x)
    elif isinstance(x, list) or isinstance(x, tuple):
      return list(map(sanitize, x))
    else:
      return None
  if isinstance(data, dict):
    return crawl(data)
  elif isinstance(data, list) or isinstance(data, tuple):
    data = filter(partial(is_not, None), map(crawl, data))
    return list(chain.from_iterable(data))

def identToQuery(data, path):
  data = isolateIdents(data, path)
  if isinstance(data, dict):
    return {'ident': data}
  elif (isinstance(data, list) or isinstance(data, tuple)) and len(data) > 0:
    idents = map(lambda x: {'ident': x}, data)
    # Remove duplicate identifiers.
    result = []
    for ident in idents:
      if ident not in result:
        result.append(ident)
    return {'$or': result}
  return None

def migrateMetainfo(schema, metainfo):
  metainfo = schema.from_dict(metainfo)

  # Normalize packages section
  if 'packages' in schema._types_map and metainfo.packages:
    for package in (metainfo.packages.helm or []):
      if package.path == None:
        package.path = f"{package.name}-{package.version}.tgz"
    for package in (metainfo.packages.raw or []):
      if package.path == None:
        package.path = f"{package.type}/{package.name}"
    for package in (metainfo.packages.yum or []):
      if package.path == None:
        package.path = f"{package.name}-{package.version}.{package.arch or 'noarch'}.rpm"

  # Normalize release section into deliverable section
  if schema == ProductSchema and metainfo.release and not metainfo.deliverable:
    servers = {
      'release_interne': f"http://cmsgvm05.gre.hpecorp.net/release/{metainfo.release.sku}/"
    }

    media = []
    for addon in metainfo.release.addons or []:
      media.append(deliverable._media(
        name=f"{addon.name}.iso",
        type='addon',
        servers=['release_interne'],
      ))
    for docset in metainfo.release.docsets or []:
      media.append(deliverable._media(
        name=f"{docset.name}.iso",
        type='docset',
        servers=['release_interne'],
      ))
    if metainfo.release.releaseNotes:
      media.append(deliverable._media(
        name="{name}_{notes}_notes-{release}-{version}.pdf".format(
            name=metainfo.release.releaseNotes.name,
            notes='release' if metainfo.scm and metainfo.scm.branch == 'master' else 'patch',
            release=metainfo.release.version,
            version=metainfo.release.releaseNotes.version,
        ),
        type='releasenotes',
        servers=['release_interne'],
      ))

    metainfo.deliverable = deliverable(
      version=metainfo.release.version,
      sku=metainfo.release.sku,
      intent='release' if metainfo.status == 'GA Released' else 'draft',
      servers=servers,
      media=media,
    )

  # Normalize history
  if 'history' in schema._types_map and metainfo.history and METAINFO_MIGRATION_HISTORY_JENKINS_BASE_URL and METAINFO_MIGRATION_HISTORY_JENKINS_BASE_URL_NHSS:
    for entry in metainfo.history:
      if entry.job != None and entry.job.id != None and entry.job.name != None and not 'url' in entry.job.as_dict():
        if entry.job.name == 'iw5g-master-nhss-promotion':
          job_base_url = METAINFO_MIGRATION_HISTORY_JENKINS_BASE_URL_NHSS
        else:
          job_base_url = METAINFO_MIGRATION_HISTORY_JENKINS_BASE_URL
        entry.job.url = job_base_url + ''.join(map(lambda i: '/job/' + i, entry.job.name.split('/'))) + '/' + entry.job.id

  return metainfo.as_dict()

def flattenDict(data, keys, values, path=[]):
  for key, value in data.items():
    if isinstance(value, list) or isinstance(value, tuple):
      continue
    elif isinstance(value, dict):
      flattenDict(value, keys, values, path + [key])
    else:
      fullkey = '.'.join((path + [key]))
      keys.add(fullkey)
      values[fullkey] = value

def toCsv(items):
  keys = set()
  data = list()
  for item in items:
    values = dict()
    flattenDict(item, keys, values)
    data.append(values)

  out = io.StringIO()
  writer = csv.DictWriter(out, fieldnames=sorted(keys), quoting=csv.QUOTE_ALL, extrasaction='ignore')
  writer.writeheader()
  writer.writerows(data)
  return out.getvalue()

def collectionResponse(result, accept):
  best_match = accept.best_match(['application/json', 'text/csv'], 'application/json')

  if best_match == 'text/csv':
    return quart.Response(
      toCsv(result['members']),
      200,
      dict(),
      'text/csv',
      'text/csv'
    )

  elif best_match == 'application/json':
    return quart.Response(
      quart.json.dumps(result),
      200,
      dict(),
      'application/json',
      'application/json'
    )

def toMermaid(graph):
  graph['links'] = list(graph['links'])

  class Node:
    def __init__(self, id, metainfo):
      self.id = id
      self.metainfo = metainfo
      self.children = []

    def __str__(self):
      name = self.metainfo['name'] or self.metainfo['ident']['artifactId']
      version = self.metainfo['ident']['version']
      if len(self.children) == 0:
        return f"{self.id}[\"{name}<br/>{version}\"]\n"
      else:
        return f"subgraph {self.id}[\"{name} ({version})\"]\n{''.join(str(child) for child in self.children)}end\n"

    def add(self, node):
      self.children.append(node)

  nodes = {k: Node(k, v) for k, v in graph['nodes'].items()}

  for linkType in ['component', 'product']:
    targetToSources = defaultdict(list)
    for link in graph['links']:
      if link['type'] == linkType:
        targetToSources[link['target']].append(link['source'])

    for target, sources in targetToSources.items():
      if len(sources) == 1:
        nodes[sources[0]].add(nodes[target])
        del nodes[target]
        graph['links'].remove({'source': sources[0], 'target': target, 'type': linkType})

  def toLink(link):
    return f"{link['source']} --> {link['target']}\n"

  renderedNodes = [str(node) for node in nodes.values()]
  renderedClasses = [f"class {key} {value['schema'].split('/')[1].split('.')[0]}\n" for key, value in graph['nodes'].items()]
  renderedLinks = [toLink(link) for link in graph['links']]

  return f"""graph LR
{''.join(renderedNodes)}

{''.join(renderedClasses)}

{''.join(renderedLinks)}

classDef product fill:#7f7
classDef solution fill:#ff7

"""

def graphResponse(graph, accept):
  best_match = accept.best_match(['text/vnd.mermaid', 'application/json'], 'application/json')

  if best_match == 'text/vnd.mermaid':
    return quart.Response(
      toMermaid(graph),
      200,
      dict(),
      'text/vnd.mermaid',
      'text/vnd.mermaid'
    )

  elif best_match == 'application/json':
    return quart.Response(
      quart.json.dumps(graph),
      200,
      dict(),
      'application/json',
      'application/json'
    )
