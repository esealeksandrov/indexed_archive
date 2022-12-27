import time

from lib.indexed_archive.archive import Archive

arch_path = "./data/test_archive/"

if __name__ == '__main__':
    arch = Archive(arch_path)
    print(arch.created_date)
    time.sleep(1)

    arch = Archive(arch_path)
    print(arch.created_date)




