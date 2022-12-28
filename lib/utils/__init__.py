import os
from typing import Any


def read_dict_field(d: dict, field: str) -> Any:
    if field in d:
        return d[field]
    return None


def path_exists(target_path: str):
    return os.path.exists(target_path)


def path_accessible(target_path: str):
    return os.access(target_path, os.R_OK | os.W_OK)
