import json
import os
import shutil
from unittest import TestCase

from lib.indexed_archive.archive_config.config import Config
from lib.indexed_archive.archive_index.index_types import IndexType
from lib.indexed_archive.archive_config.exceptions import ArchiveConfigFileCreateException


class ArchiveConfigTest(TestCase):
    test_data = {
        "root_path": "./data",
        "archive_id": "120932388123",
        "index_type": IndexType.JSON,
        "description": "aboutvonfig",
    }

    def test_create_new_config_file(self):
        root = os.path.abspath(self.test_data["root_path"])
        arch_id = self.test_data["archive_id"]
        archive_path = os.path.join(root, arch_id)
        config_path = os.path.join(archive_path, "config.json")
        description = self.test_data["description"]
        index_type = self.test_data["index_type"]
        if os.path.exists(archive_path):
            shutil.rmtree(archive_path)
        with self.assertRaises(ArchiveConfigFileCreateException):
            Config.create(root, arch_id, index_type, description)
        os.mkdir(archive_path)
        Config.create(root, arch_id, index_type, description)
        with open(config_path) as config_file:
            data = json.loads(config_file.read())
            self.assertEqual(data["id"], arch_id)
            self.assertEqual(IndexType(data["index_type"]), index_type)
            self.assertEqual(data["description"], description)
        shutil.rmtree(archive_path)

    def test_init_config(self):
        # good test
        ...

    def test_to_dict(self):
        ...

