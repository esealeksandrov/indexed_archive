"""
Config - an entity, that contains archive configuration information in json file above archive.
Class Config - proxy to config file.
Config:
    fields:
        id: str
        created_date: int -> datetime
        updated_date: int -> datetime
        index_type: IndexType
        description: str | None
"""
import datetime
import json
import os.path

from lib.indexed_archive.core.file import File
from lib.constants import DEFAULT_ENCODING
from lib.indexed_archive.archive_index.index_types import IndexType
from lib.indexed_archive.archive_config.exceptions import (
    ArchiveConfigFieldReadException,
    ArchiveConfigFileWriteException,
    ArchiveConfigFieldException,
    ArchiveConfigFileCreateException
)


class Config(File):
    def __init__(self, archive_path: str):
        super(Config, self).__init__(os.path.join(archive_path, "config.json"))
        # need initialization
        self._id: str = None
        self._created_date: int = None
        self._updated_date: int = None
        self._index_type: IndexType = None
        self._description: str = None
        self._init_from_file()

    @classmethod
    def create(cls, root_path: str, arch_id: str, index_type: IndexType, description: str = None):
        current_date = datetime.datetime.now().timestamp()
        config_file_path = os.path.join(os.path.join(os.path.abspath(root_path), str(arch_id)), "config.json")
        config_data = {
            "id": arch_id,
            "created_date": current_date,
            "updated_date": current_date,
            "index_type": index_type,
            "description": description
        }
        try:
            with open(config_file_path, "w", encoding=DEFAULT_ENCODING) as config_file:
                config_file.write(json.dumps(config_data))
        except Exception as e:
            raise ArchiveConfigFileCreateException(f"Can't create config file ({config_file_path}): {e}")

    def _init_from_file(self):
        try:
            config_data = self._get_config_data()
            self._id = config_data["id"]
            self._created_date = config_data["created_date"]
            self._updated_date = config_data["updated_date"]
            self._index_type = IndexType(config_data["index_type"])
            self._description = config_data["description"]
        except Exception as e:
            raise ArchiveConfigFieldException(f"Can't init field of config file({self._config_path}): {e}")



    def _get_field(self, field_name: str):
        config_data = self._get_config_data()
        if field_name in config_data:
            return config_data[field_name]
        return None

    def _get_config_data(self) -> dict:
        try:
            return json.loads(self.read())
        except Exception as e:
            raise ArchiveConfigFieldReadException(f"Can't read configfile ({self.config_path}): {e}")

    def _save_config_data(self):
        self._updated_date = datetime.datetime.now().timestamp()
        try:
            self.write(json.dumps(self._to_dict()))
        except Exception as e:
            raise ArchiveConfigFileWriteException(f"Can't write config file({self._path}): {e}")

    def _to_dict(self):
        return {
            "id": self._id,
            "created_date": self._created_date,
            "update_date": self._updated_date,
            "description": self._description,
            "index_type": self._index_type
        }

    @property
    def config_path(self):
        return self._path

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, arch_id: str):
        if not isinstance(arch_id, str):
            raise ValueError(f"Config field id must be string, not {type(arch_id)}")
        self._id = arch_id
        self._save_config_data()

    @property
    def created_date(self) -> datetime.datetime:
        return datetime.datetime.fromtimestamp(self._created_date)

    @created_date.setter
    def created_date(self, created_date: datetime.datetime):
        if not isinstance(created_date, datetime.datetime):
            raise ValueError(f"Config field created_date must be datetime object, not {type(created_date)}")
        self._created_date = created_date.timestamp()
        self._save_config_data()

    @property
    def update_date(self) -> datetime.datetime:
        return datetime.datetime.fromtimestamp(self._updated_date)

    @property
    def description(self) -> str:
        return self._description if self._description is not None else ""

    @description.setter
    def description(self, description: str | None):
        if not isinstance(description, str):
            raise ValueError(f"Config field description must be str, not {type(description)}")
        self._description = description
        self._save_config_data()

    @property
    def index_type(self) -> IndexType:
        return IndexType(self._index_type)

    @index_type.setter
    def index_type(self, index_type: IndexType):
        if type(index_type) == IndexType:
            raise ValueError(f"Config field index_type must be IndexType, not {type(index_type)}")
        self._index_type = index_type
        self._save_config_data()


