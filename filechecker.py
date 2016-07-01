import os
import hashlib
import random
from checkfile import *

class FileChecker:

    def __init__(self, info_path, info_checksum, info_size):
        self.info_path = info_path
        self.info_name = os.path.basename(info_path)
        self.info_checksum = info_checksum
        self.info_size = info_size

    def test_file_present(self):
        return os.path.isfile(self.info_path)

    def test_md5sum(self):
        file_md5sum = hashlib.md5(open(self.info_path, 'rb').read()).hexdigest()
        given_md5sum = self.info_checksum
        return file_md5sum == given_md5sum

    def test_size(self):
        file_size = os.path.getsize(self.info_path)
        given_size = int(self.info_size)
        return file_size == given_size

if __name__ == "__main__":
    positive_test = FileChecker('data/omni_20160622-000000-lookup_data.tar.gz', '1b8307f057dbd01be01117f39ffead77', 478)
    if positive_test.test_file_present():
        print "File present"
    else:
        print("File not present - this shouldn't have happened")
    if positive_test.test_md5sum():
        print "Checksum ok"
    else:
        print("Checksum not ok - this shouldn't have happened")
    if positive_test.test_size():
        print "Size ok"
    else:
        print("Size not ok - this shouldn't have happened")

    file_not_present_test = FileChecker('data/xxomni_20160622-000000-lookup_data.tar.gz', '1b8307f057dbd01be01117f39ffead77', 478)
    if file_not_present_test.test_file_present():
        print "File present - this should not have happened"
    else:
        print("File not present - this is ok in this test")

    checksum_not_ok_test = FileChecker('data/omni_20160622-000000-lookup_data.tar.gz', '1b8307f057dbd01be01117f39ffead78', 478)
    if checksum_not_ok_test.test_md5sum():
        print "Checksum ok - this should not have happened"
    else:
        print("Checksum not ok - this is ok in this test")

    size_not_ok_test = FileChecker('data/omni_20160622-000000-lookup_data.tar.gz', '1b8307f057dbd01be01117f39ffead77', 479)
    if size_not_ok_test.test_size():
        print("File size ok - this shouldn't have happened")
    else:
        print("Size not ok - this is ok in this test")

