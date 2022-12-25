"""
archive - an entity that contains information about the archive and search index.
Class:
    fields:
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


class Archive:
    def __init__(self, archive_path: str):
        self.path = os.path.abspath(archive_path)
        self.config = os.path.join(self.path, "config.json")
