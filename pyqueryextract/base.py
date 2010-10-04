from pyquery import PyQuery


class QueryMiss(Exception):
    pass


def query_op(d, spec):
    """ Example query:
    {"$query": "a"}

    or 

    {"$query": "a",
     "$op": ["attr", "href"]}
    """
     
    query = spec['$query']
    
    if "$op" in spec:
        op = spec['$op']
    else:
        op = ['html']
    
    match = d(query)

    if len(match) == 0:
        raise QueryMiss(query)

    # Get the op details

    # If the length of the match is only 1, apply the operation and return
    # the result
    if len(match) == 1:
        func = getattr(match, op[0])
        args = op[1:]

        return func(*args)

    # If the length of the match is greater than 1, apply the opperation to
    # each element
    else:
        result = []

        for el in match:
            item = PyQuery(el)
            func = getattr(item, op[0])
            args = op[1:]
            
            result.append(func(*args))
        return result
            

OPERATION_MAP = {
    '$query': query_op,
}


def find_op(spec):
    operation = None
    for op in OPERATION_MAP.keys():
        if op in spec:
            operation = OPERATION_MAP[op]
            break
    return operation


def extract(d, spec):
    result = {}
    for key, val in spec.iteritems():
        if type(val) is dict:
            # Locate which operator to use
            operation = find_op(val)
        
            if operation is not None:
                val = operation(d, val)

        result[key] = val

    return result
