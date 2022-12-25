from typing import Any


def read_dict_field(d: dict, field: str) -> Any:
    """Util function for read index_archive config file data fields"""
    if field in d:
        return d[field]
    return None
