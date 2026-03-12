schema_cache = {}

def get_schema(dataset):

    return schema_cache.get(dataset)


def set_schema(dataset, schema):

    schema_cache[dataset] = schema