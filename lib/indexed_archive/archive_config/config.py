"""
Config - an entity, that contains archive configuration information in json file above archive.
ConfigData:
    fields:
        id: str
        index_type: ConfigType

"""


import os
import json

from lib.constants import DEFAULT_ENCODING
from lib.utils import read_dict_field
from lib.indexed_archive.archive_config.exceptions import (
    ConfigReadException,
    ConfigWriteException,
    ConfigFieldException
)
from lib.indexed_archive.archive_config.config_types import IndexType

class ConfigData:
    """
    Class for manipulation config data.
    It's init all class fields in dict,
    and serialize it to dict
    """
    def __init__(self):
        self.id: str = None
        self.index_type: ConfigTypes = None

    def get_fields(self):
        return tuple(filter(lambda k: not k.startswith("_"), self.__dict__.keys()))

    def init_config(self, config_data: dict):
        for field_name in self.get_fields():
            self.__dict__[field_name] = read_dict_field(config_data, field_name)

    def to_dict(self):
        return {k: v for k, v in self.__dict__ if not k.startswith("_")}


class Config:
    """Class for manipulation archive configuration"""
    def __init__(self, path: str):
        self._path: str = os.path.abspath(path)
        self._config_data: ConfigData = ConfigData()
        self._init_config_file()

    def _init_config_file(self):
        """send dict with none values to json file"""
        if not os.path.exists(self._path) or not os.path.isfile(self._path):
            self._write_config()

    def _read_config(self):
        try:
            with open(self._path, "r", encoding=DEFAULT_ENCODING) as config_file:
                self._config_data.init_config(json.loads(config_file.read()))
        except Exception as e:
            raise ConfigReadException(f"Can't read config file: {e}")

    def _write_config(self):
        try:
            with open(self._path, "w", encoding=DEFAULT_ENCODING) as config_file:
                config_file.write(json.dumps(self._config_data.to_dict()))
        except Exception as e:
            raise ConfigWriteException(f"Can't save config file: {e}")

    def _validate_field(self, key):
        if key not in self._config_data.get_fields():
            raise ConfigFieldException(f"There is no filed with name '{key}'")

    def __getattr__(self, item):
        self._validate_field(item)
        return self._config_data.__dict__[item]

    def __getattribute__(self, item):
        return None

    def __setattr__(self, key, value):
        self._validate_field(key)
        self._config_data.__dict__[key] = value
