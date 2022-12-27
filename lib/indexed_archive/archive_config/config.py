"""
Config - an entity, that contains archive configuration information in json file above archive.
ConfigData:
    fields:
        id: str
        created_date: int
        index_type: ConfigType
"""


import os
import json
from datetime import datetime

from lib.constants import DEFAULT_ENCODING
from lib.utils import read_dict_field
from lib.indexed_archive.archive_config.exceptions import (
    ArchiveConfigFileCreateException,
    ArchiveConfigFieldReadException,
    ArchiveConfigFileWriteException,
    ArchiveConfigFieldFileException,
    ArchiveConfigFileNotValid
)
from lib.indexed_archive.archive_config.config_types import IndexType


class ConfigData:
    """
    Class for manipulation config data.
    It's init all class fields in dict,
    and serialize it to dict
    """
    def __init__(self):
        self._is_inited = False
        self.id: str = None
        self.created_date: int = datetime.now().timestamp()
        self.index_type: IndexType = None

    def get_fields(self):
        return tuple(filter(lambda k: not k.startswith("_"), self.__dict__.keys()))

    def init_config(self, config_data: dict):
        if not isinstance(config_data, dict):
            raise ValueError
        for field_name in self.get_fields():
            self.__dict__[field_name] = read_dict_field(config_data, field_name)
        self._is_inited = True

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}


class Config:
    """Class for manipulation archive configuration"""
    def __init__(self, archive_path: str):
        self._config_file_path: str = os.path.abspath(os.path.join(archive_path, "config.json"))
        self._config_data: ConfigData = ConfigData()
        self._init_config_file()

    def is_config_file_exists(self):
        return os.path.exists(self._config_file_path)

    def is_config_file_accessible(self):
        return os.access(self._config_file_path, os.R_OK | os.W_OK)

    def _init_config_file(self):
        """check config file, try to read."""
        if self.is_config_file_exists():
            if not self.is_config_file_accessible():
                raise ArchiveConfigFieldReadException(f"Can't read/write config file ({self._config_file_path}): "
                                                      f"file not accessible")
            config_data = self._read_config_data()
            if config_data is None:
                self._write_config_data()
            self._config_data.init_config(self._read_config_data())
        else:
            self._write_config_data()

    def _read_config_data(self):
        if not self.is_config_file_exists():
            raise ArchiveConfigFieldReadException(f"Can't read config file({self._config_file_path}): "
                                                  f"it's not accessible")
        with open(self._config_file_path, "r", encoding=DEFAULT_ENCODING) as config_file:
            try:
                return json.loads(config_file.read())
            except json.JSONDecodeError as e:
                ArchiveConfigFieldReadException(f"Can't decode config file({self._config_file_path}): {e}")
        return None

    def _write_config_data(self):
        with open(self._config_file_path, "w", encoding=DEFAULT_ENCODING) as config_file:
            config_file.write(json.dumps(self._config_data.to_dict()))

    # config data proxy fields

    def __getattr__(self, item):
        if item in self._config_data.get_fields():
            return self._config_data.__dict__[item]
        return self.__dict__[item]

