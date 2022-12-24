import os


class Archive:
    def __init__(self, archive_path: str):
        self.path = os.path.abspath(archive_path)
        self.config = os.path.join(self.path, "config.json")
