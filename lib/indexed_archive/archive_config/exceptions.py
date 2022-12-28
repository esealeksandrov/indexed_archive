"""
All IndexArchive exceptions
"""


class ArchiveConfigException(Exception):
    ...


class ArchiveConfigFileException(ArchiveConfigException):
    ...


class ArchiveConfigDirectoryException(ArchiveConfigException):
    ...


class ArchiveConfigFileCreateException(ArchiveConfigFileException):
    ...


class ArchiveConfigDirectoryCreateException(ArchiveConfigDirectoryException):
    ...


class ArchiveConfigFieldReadException(ArchiveConfigFileException):
    ...


class ArchiveConfigFileWriteException(ArchiveConfigFileException):
    ...


class ArchiveConfigFieldFileException(ArchiveConfigFileException):
    ...

class ArchiveConfigFileNotValid(ArchiveConfigFileException):
    ...
