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
        ...
"""


import os
from lib.indexed_archive.exceptions import (
    ArchiveCreateDirException
)

from lib.indexed_archive.archive_config.config import Config


class Archive:
    def __init__(self, archive_path: str):
        self._id = None
        self._archive_path = os.path.abspath(archive_path)
        self._config: Config = None
        self.init_archive_directory()
        self.init_archive_config()

    @property
    def id(self):
        return self._config.id

    @id.setter
    def id(self, value):
        self._config.id = value


    @property
    def created_date(self):
        return self._config.created_date

    def is_directory_exists(self):
        return os.path.exists(self._archive_path)

    def is_directory_accessible(self):
        return os.path.isdir(self._archive_path) and os.access(self._archive_path, os.R_OK | os.W_OK)

    def init_archive_directory(self):
        if not self.is_directory_exists():
            try:
                os.mkdir(self._archive_path)
            except Exception as e:
                raise ArchiveCreateDirException(f"Can't create archive directory ({self._archive_path}): {e}")
        if not self.is_directory_accessible():
            raise ArchiveCreateDirException(f"Can't create archive directory ({self._archive_path}): "
                                            f"path not accessible")

    def init_archive_config(self):
        self._config = Config(self._archive_path)





