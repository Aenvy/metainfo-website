def _toType(t):
    if t == str:
        return 'string'
    elif t == bool:
        return 'boolean'
    elif t == dict:
        return 'object'
    elif t == list:
        return 'array'

def _toObject(valType, valSubtype):
    if valType in [bool, str]:
        return {'type': _toType(valType)}
    elif valType == list:
        return {'type': _toType(valType), 'subtype': _toObject(valSubtype, None)}
    elif hasattr(valType, '_types_map'):
        return {'type': {k: _toObject(v['type'], v['subtype']) for (k, v) in valType._types_map.items()}}
    #    else:
    #      raise RuntimeError('Unable to convert ({}, {}) at "{}" to schema'.format(valType, valSubtype, path))

def schema2json(schema):
    return _toObject(schema, None)['type']
