from unittest import TestCase, main

from lib.indexed_archive.config import ConfigData


class ArchiveConfigTest(TestCase):
    def test_get_fields(self):
        test_config_data = ConfigData()
        expected_fields = ("id", "name", "index_type")
        self.assertEqual(test_config_data.get_fields(), expected_fields)

    def test_init_config(self):
        test_config_data = ConfigData()
        self.assertEqual(1, 2)

    def test_to_dict(self):
        test_config_data = ConfigData()
        self.assertEqual(1, 2) 

