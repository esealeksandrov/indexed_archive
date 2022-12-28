"""
archive - an entity that contains information about the archive and search index.
It's a directory with config, indexes file, log files and data files.
Class:
    fields:
        id: str (uniq id_string)
        name: str (archive name)
        created_date: int (created_date timestamp)
        path: str (path to archive directory + id)
        size: int (sum of archive data size and index data size. It's calculate with write archive data and index)
        config: Config (object containing configuration of archive)
        index: IndexData (object containing Index data for search)
        data: ArchiveData (
            object containing archived data.
            Archived_data - it's a zipped text data
        )
        log: ArchiveLog (
            object containing logs.
            Logs - it's a list of messages/lines waiting to be archived
        )
    functions:
        create
        update
        delete
"""
import os

from datetime import datetime
from lib.indexed_archive.exceptions import (
    ArchiveCreateDirException,
    ArchiveInvalidPath
)
from lib.indexed_archive.archive_config.config import Config
from lib.indexed_archive.archive_config.config_types import IndexType
from lib.indexed_archive.archive_index.index import Index
from lib.indexed_archive.archive_log.log import Log

from lib.utils import (
    path_exists,
    path_accessible
)

class Archive:
    def __init__(self, archive_path: str):
        self._archive_path: str = os.path.abspath(archive_path)
        self._config: Config = Config(self._archive_path)
        self._log: Log = Log(self._archive_path)
        self._index: Index = Index(self._archive_path)
        self._validate_archive()

    def _validate_archive(self):
        if not path_exists(self._archive_path) or not path_accessible(self._archive_path):
            error_message = f"Root archive directory ({self._archive_path}) not available"
            raise ArchiveInvalidPath(error_message)
        self._config.validate()
        self._index.validate()
        self._log.validate()



    @classmethod
    def create(cls, root_path: str, archive_id: str, index_type: IndexType, description: str = None):
        created_date = datetime.now()
        root_path = os.path.abspath(root_path)
        archive_path = cls.create_archive_directory(root_path, str(archive_id))
        Config.create(archive_path, archive_id, index_type, description)
        Index.create(archive_path, index_type)
        Log.create(archive_path)
        return cls(archive_path)

    @classmethod
    def create_archive_directory(cls, root_path: str, archive_id: str):
        archive_path = os.path.join(root_path, str(archive_id))
        if not path_exists(root_path) and not path_accessible(root_path):
            raise ArchiveCreateDirException(f"Can't create archive dir ({archive_path}): root not accessible")
        try:
            os.mkdir(archive_path)
        except Exception as e:
            raise ArchiveCreateDirException(f"Can't create archive dir ({archive_path}): {e}")
        return archive_path

    def delete(self):
        try: os.rmdir(self._archive_path)
        except Exception as e:
            print("joijdoqwijdoijqw")

# class Archive:
#     def __init__(self, archive_path: str):
#         self._id = None
#         self._archive_path = os.path.abspath(archive_path)
#         self._config: Config = None
#         self.init_archive_directory()
#         self.init_archive_config()
#
#     @staticmethod
#     def create(id: int, root_path: str, description: str = None):
#         return Archive()
#
#     @property
#     def id(self):
#         return self._config.id
#
#     @id.setter
#     def id(self, value):
#         self._config.id = value
#
#
#     @property
#     def created_date(self):
#         return self._config.created_date
#
#     def is_directory_exists(self):
#         return os.path.exists(self._archive_path)
#
#     def is_directory_accessible(self):
#         return os.path.isdir(self._archive_path) and os.access(self._archive_path, os.R_OK | os.W_OK)
#
#     def init_archive_directory(self):
#         if not self.is_directory_exists():
#             try:
#                 os.mkdir(self._archive_path)
#             except Exception as e:
#                 raise ArchiveCreateDirException(f"Can't create archive directory ({self._archive_path}): {e}")
#         if not self.is_directory_accessible():
#             raise ArchiveCreateDirException(f"Can't create archive directory ({self._archive_path}): "
#                                             f"path not accessible")
#
#     def init_archive_config(self):
#         self._config = Config(self._archive_path)





