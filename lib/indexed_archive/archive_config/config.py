"""
Config - an entity, that contains archive configuration information in json file above archive.
ConfigData:
    fields:
        id: str
        created_date: int
        index_type: ConfigType
"""
import datetime
import json
import os.path

from lib.constants import DEFAULT_ENCODING
from lib.indexed_archive.archive_config.config_types import IndexType
from lib.indexed_archive.archive_config.exceptions import (
    ArchiveConfigFieldReadException
)

class Config:
    def __init__(self, archive_path: str):
        self.__archive_path: str = os.path.abspath(archive_path)

        self._id: str = None
        self._created_date = None
        self._updated_date: datetime.datetime = None
        self._index_type: IndexType
    @property
    def config_path(self):
        return os.path.join(self.__archive_path, "config.json")


    def _get_field(self, field_name: str):
        with open(config_file_path, "r", encoding=DEFAULT_ENCODING) as config_file:
            return json.decode(config_file.read())

    def _read_config_file(self):
        try:
            with open(self.config_path, "r", encoding=DEFAULT_ENCODING) as config_file:
                return json.loads(config_file.read())
        except Exception as e:
            raise ArchiveConfigFieldReadException(f"Can't read configfile ({self.config_path}): {e}")

