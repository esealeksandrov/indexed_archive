import json
import os.path
import time

from lib.indexed_archive.archive import Archive
from lib.indexed_archive.archive_config.config import Config
from lib.indexed_archive.archive_index.index_types import IndexType

arch_path = "./data/"
arch_id = "10"
arch_index_type = IndexType.JSON
arch_desc = "92138"


if __name__ == '__main__':
    # arch = Archive.create(arch_path, "10", IndexType.JSON, "owiejoiwejdowejdio")
    Config.create(arch_path, arch_id, arch_index_type, arch_desc)

    conf = Config(os.path.join(arch_path, arch_id))

    print(conf.id)
    conf.id = '3123123'
    print(conf.id)
    with open(os.path.join(arch_path, arch_id, "config.json"), "r") as file:
        print(json.loads(file.read()))
    # print(arch.created_date)
    # time.sleep(1)
    #
    # arch = Archive(arch_path)
    # print(arch.created_date)




