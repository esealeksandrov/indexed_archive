"""
All IndexArchive exceptions
"""


class ArchiveConfigFileException(Exception):
    ...


class ArchiveConfigFileCreateException(ArchiveConfigFileException):
    ...


class ArchiveConfigFieldReadException(ArchiveConfigFileException):
    ...


class ArchiveConfigFileWriteException(ArchiveConfigFileException):
    ...


class ArchiveConfigFieldFileException(ArchiveConfigFileException):
    ...

class ArchiveConfigFileNotValid(ArchiveConfigFileException):
    ...
