import os
import time
import threading
from threading import RLock

from lib.constants import DEFAULT_ENCODING


class File:
    instances = {}

    def __new__(cls, path: str, *args, **kwargs):
        file_path = os.path.abspath(path)
        if file_path not in cls.instances:
            cls.instances[file_path] = super().__new__(cls)
        return cls.instances[file_path]

    def __init__(self, path: str):
        self._lock = RLock()
        self._path = os.path.abspath(path)

    def write(self, data: str | bytes, encoding: str = DEFAULT_ENCODING):
        with self._lock:
            mode = "wb" if isinstance(data, bytes) else "w"
            with open(self._path, mode, encoding=encoding) as file:
                file.write(data)

    def read(self) -> str | bytes:
        with self._lock:
            with open(self._path, encoding=DEFAULT_ENCODING) as file:
                return file.read()
