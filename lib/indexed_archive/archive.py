"""
archive - an entity that contains information about the archive and search index.
Class:
    fields:
        name: str (archive name)
        created_date: int (created_date timestamp)
        id: str (uniq id_string)
        path: str (path to archive file.)
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
from lib.indexed_archive.archive_config.config import Config


class Archive:
    def __init__(self, name: str, archive_path: str):
        self._name = name
        self._path = os.path.abspath(archive_path)
        self._config = Config(self.path)

    def _init_archive_path(self):
        ...

