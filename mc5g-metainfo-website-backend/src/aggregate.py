import functools

def _get(subtree, path):
    # FIXME: ident.version subfields not computed correctly.
    # (for example with 1.63.0-1-yyymmddHHMMSS, ident.version:version should be 1.63.0-1)
    if path == 'ident.version:version':
        return '-'.join(subtree['ident']['version'].split('-')[:1])
    elif path == 'ident.version:date':
        return '-'.join(subtree['ident']['version'].split('-')[:2])

    for key in path.split('.'):
        if not isinstance(subtree, dict):
            return None
        if not key in subtree:
            return None

        subtree = subtree[key]

    if not isinstance(subtree, str):
        return None

    return subtree

def _metainfoToAggregate(metainfo, keys):
    return tuple(_get(metainfo, key) for key in keys)

def _compareVersion(aVersion, bVersion):
    aVersion = tuple(tuple(int(field) for field in part.split('.')) for part in aVersion.split('-'))
    bVersion = tuple(tuple(int(field) for field in part.split('.')) for part in bVersion.split('-'))
    numCommonParts = min(len(aVersion), len(bVersion))

    for indexPart in range(0, numCommonParts):
        aPart = aVersion[indexPart]
        bPart = bVersion[indexPart]
        numCommonFields = min(len(aPart), len(bPart))

        for fieldPart in range(0, numCommonFields):
            aField = aPart[fieldPart]
            bField = bPart[fieldPart]

            if aField != bField:
                return aField - bField
        
        if len(aPart) - len(bPart) != 0:
            return len(aPart) - len(bPart)
    
    return len(aVersion) - len(bVersion)

def _metainfosFor(collection, keys, isBetterThan):
    aggregates = dict()
    for candidateMetainfo in collection:
        candidateAggregate = _metainfoToAggregate(candidateMetainfo, keys)
        metainfo = aggregates.get(candidateAggregate, None)

        if metainfo == None or (metainfo != None and isBetterThan(candidateMetainfo['ident']['version'], metainfo['ident']['version'])):
            aggregates[candidateAggregate] = candidateMetainfo
    
    return tuple(val for val in aggregates.values())

def earliestMetainfosFor(collection, keys):
    return _metainfosFor(collection, keys, lambda a, b : _compareVersion(a, b) < 0)

def latestMetainfosFor(collection, keys):
    return _metainfosFor(collection, keys, lambda a, b: _compareVersion(a, b) > 0)

def _cmp(a, b):
    return (a > b) - (a < b)

def sortMetainfosBy(collection, keys):
    sortFns = []
    for key in reversed(keys):
        if key.endswith(':descending'):
            key = key[:-11]
            reverse = True
        else:
            if key.endswith(':ascending'):
                key = key[:-10]
            reverse = False

        if key == 'ident.version':
            if reverse:
                fn = lambda a, b, key=key: -_compareVersion(_get(a, key), _get(b, key))
            else:
                fn = lambda a, b, key=key: _compareVersion(_get(a, key), _get(b, key))
        else:
            if reverse:
                fn = lambda a, b, key=key: -_cmp(_get(a, key), _get(b, key))
            else:
                fn = lambda a, b, key=key: _cmp(_get(a, key), _get(b, key))

        sortFns.append(fn)

    def sortFn(a, b):
        for fn in sortFns:
            result = fn(a, b)
            if result != 0:
                return result
        return 0

    return sorted(collection, key=functools.cmp_to_key(sortFn))
