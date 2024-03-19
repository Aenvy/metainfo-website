#!/usr/bin/python3

import re

def _pathToStr(path) -> str:
    return '.'.join(path) or '.'

class OneOfAllowedError(RuntimeError):
  def __init__(self, path, validValues):
    super().__init__('Only one of {} is allowed inside query object for property {}'.format(', '.join(validValues), _pathToStr(path)))

class InvalidType(RuntimeError):
  def __init__(self, path, badType, expectedType):
    super().__init__('Invalid type {} for property {}, expected type {}'.format(badType.__name__, _pathToStr(path), expectedType.__name__))

class InvalidKey(RuntimeError):
  def __init__(self, path, propertyType, badKey):
    super().__init__('Invalid key {} for property {} of type {}'.format(badKey, _pathToStr(path), propertyType.__name__))

class OperatorRequiresListOf(RuntimeError):
  def __init__(self, path, operator, schema):
    super().__init__('Operator {} requires list of {} for property {}'.format(operator, schema.__name__, _pathToStr(path)))

class OperatorRequiresAtomicProperty(RuntimeError):
  def __init__(self, path, operator, schema):
    super().__init__('Operator {} cannot be applied to non-atomic type {} for property {}'.format(operator, schema.__name__, _pathToStr(path)))

class _Subquery:
  _LIST_OPERATORS={
    '$allOf',
    '$anyOf'
  }

  def __init__(self, schema, value, path):
    self._allOfClauses = []
    self._anyOfClauses = []
    regularClauses = self._compileObject(schema, path, value)

    self._compiledSubquery = { k: v for (k, v) in regularClauses }

    if len(self._anyOfClauses) > 0 or len(self._allOfClauses) > 0:
      self._compiledSubquery['$and'] = [ { '$or': anyOfClause } for anyOfClause in self._anyOfClauses ] + self._allOfClauses

  def getCompiledSubquery(self):
    return self._compiledSubquery

  def _compileAtomicProp(self, schema, path, value):
    return ((_pathToStr(path), self._compileValue(schema, path, value)),)

  def _compileValue(self, schema, path, value):
    if isinstance(value, str) and schema == str and len(value) >= 2 and value[0] == '/' and value[-1] == '/':
      return re.compile(value[1:-1])
    if isinstance(value, schema):
      return value

    raise InvalidType(path, type(value), schema)

  def _compileList(self, schema, path, value):
    realSchema = schema
    if not realSchema in (str, bool):
      realSchema = dict

    if isinstance(value, dict):
      keys = value.keys()
      if len(_Subquery._LIST_OPERATORS & keys) == 0 or len(keys) != 1:
        raise OneOfAllowedError(path, _Subquery._LIST_OPERATORS)

      operator = list(keys)[0]
      items = value[operator]
      if not isinstance(items, list) or any(not isinstance(item, realSchema) for item in items):
        raise OperatorRequiresListOf(path, operator, schema)

      if realSchema == dict:
        clauses = []
        for item in items:
          clauses.append({ k: v for (k, v) in [ i for prop, value in item.items() for i in self._compileObjectProp(schema, [], prop, value) ] })

        if operator == '$anyOf':
          self._anyOfClauses.append([ { _pathToStr(path): { '$elemMatch': clause } } for clause in clauses ])
        elif operator == '$allOf':
          self._allOfClauses.extend([ { _pathToStr(path): { '$elemMatch': clause } } for clause in clauses ])
      else:
        clauses = [self._compileValue(realSchema, path, item) for item in items]

        if operator == '$anyOf':
          return ((_pathToStr(path), {'$in': clauses}),)
        elif operator == '$allOf':
          return ((_pathToStr(path), {'$all': clauses}),)

      return []

    raise InvalidType(path, type(value), schema)

  def _compileObjectProp(self, schema, path, prop: str, value):
    if prop not in schema._types_map.keys():
      raise InvalidKey(path, schema, prop)

    propType = schema._types_map[prop]['type']
    if propType == list:
      return self._compileList(schema._types_map[prop]['subtype'], path + [prop], value)
    elif propType in (str, bool):
      return self._compileAtomicProp(propType, path + [prop], value)
    elif isinstance(value, dict):
      return self._compileObject(propType, path + [prop], value)

    raise InvalidType(path, type(value), schema)
    
  def _compileObject(self, schema, path, obj: dict):
    return [ i for prop, value in obj.items() for i in self._compileObjectProp(schema, path, prop, value) ]

class Query:
  _BOOLEAN_OPERATORS={
    '$and',
    '$not',
    '$or'
  }

  def __init__(self, schema, query: dict):
    self.schema = schema
    self.query = query

  def getCompiledQuery(self, path=[]) -> dict:
    return self._compileSubquery(path, self.query, self.schema)

  def _compileSubquery(self, path, query, schema):
    if not isinstance(query, dict):
      raise RuntimeError('Expected an object at root or boolean operator object')

    keys = query.keys()
    if len(Query._BOOLEAN_OPERATORS & keys) > 0:
      if len(keys) > 1:
        raise RuntimeError('Only one of {} is allowed inside root or boolean operator object'.format(', '.join(Query._BOOLEAN_OPERATORS)))

      operator = list(keys)[0]
      if operator == '$not':
        return {
          '$not': Query(schema, query[operator]).getCompiledQuery()
        }
      return {
        operator: [Query(schema, i).getCompiledQuery() for i in query[operator]]
      }

    return _Subquery(schema, query, path).getCompiledSubquery()
