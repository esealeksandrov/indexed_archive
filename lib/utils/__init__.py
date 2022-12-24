def read_dict_field(field, d):
    """Util function for read index_archive config file data fields"""
    if field in d:
        return d[field]
    return None
