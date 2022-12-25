"""
All IndexArchive exceptions
"""


class ConfigException(Exception):
    ...

class ConfigFieldReadException(ConfigException):
    ...


class ConfigReadException(ConfigException):
    ...


class ConfigWriteException(ConfigException):
    ...


class ConfigFieldException(ConfigException):
    ...
