from lib.indexed_archive.archive_index.index_types import IndexType


class Index:
    def __int__(self):
        ...

    def _validate(self):
        ...

    @classmethod
    def create(cls, archive_path: str, index_type: IndexType):
        ...