from unittest import TestCase

from lib.indexed_archive.archive_config.config import ConfigData


class ArchiveConfigTest(TestCase):
    def test_get_fields(self):
        test_config_data = ConfigData()
        expected_fields = ("id", "name", "index_type")
        self.assertEqual(test_config_data.get_fields(), expected_fields)

    def test_init_config(self):
        # good test
        test_config_data = ConfigData()
        test_config_data.init_config({
            "id": "1",
            "name": "first_test_name",
            "index_type": "json2d"
        })
        self.assertEqual(test_config_data.id, "1")
        self.assertEqual(test_config_data.name, "first_test_name")
        self.assertEqual(test_config_data.index_type, "json2d")

        test_config_data.name = "second_test_name"
        self.assertEqual(test_config_data.name, "second_test_name")

        test_config_data = ConfigData()
        test_config_data.init_config({
            "id": "1",
            "name": "test_name"
        })
        self.assertEqual(test_config_data.index_type, None)




    def test_to_dict(self):
        test_config_data = ConfigData()
        # self.assertEqual(1, 2)

