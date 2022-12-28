import time

from lib.indexed_archive.archive import Archive
from lib.indexed_archive.archive_config.config_types import IndexType

arch_path = "./data/"



if __name__ == '__main__':
    arch = Archive.create(arch_path, "10", IndexType.JSON, "owiejoiwejdowejdio")
    print(arch.created_date)
    time.sleep(1)

    arch = Archive(arch_path)
    print(arch.created_date)




