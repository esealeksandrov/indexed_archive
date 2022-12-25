from unittest import TestCase

from lib.utils import read_dict_field


class TestUtils(TestCase):
    def test_read_dict_field(self):
        test_data = {"name": "John", "sname": "Doe"}
        # Good test
        self.assertEqual(read_dict_field(test_data, "name"), "John")

        # Good test
        self.assertEqual(read_dict_field(test_data, "age"), None)
