import os.path
from unittest import TestCase, main
from lib.indexed_archive.archive import Archive


class ArchiveTest(TestCase):
    def test_archive_initialization(self):
        test_archive = Archive(".")
        right_path = os.path.abspath(".")
        self.assertEqual(test_archive.path, right_path)

# if __name__ == "__main__":
#     from pprint import pprint