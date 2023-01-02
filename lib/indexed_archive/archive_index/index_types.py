from enum import Enum


class IndexType(str, Enum):
    JSON: str = "json"
    JSON2D: str = "json2d"
    TEXT: str = "text"
    BYTES: str = "bytes"

