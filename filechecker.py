# -*- coding: utf-8 -*-
import os
import hashlib

class FileChecker(object):
    """
    Several fit tests comparing file information and files
    """

    def __init__(self, info_path, info_checksum, info_size):
        self.info_path = info_path
        self.info_name = os.path.basename(info_path)
        self.info_checksum = info_checksum
        self.info_size = info_size

    def test_file_present(self):
        """ Check if file is present in filesystem """
        return os.path.isfile(self.info_path)

    def test_md5sum(self):
        """ Check md5sum against given file information """
        file_md5sum = hashlib.md5(open(self.info_path, 'rb').read()).hexdigest()
        given_md5sum = self.info_checksum
        return file_md5sum == given_md5sum

    def test_size(self):
        """ Check if file size matches given file size """
        file_size = os.path.getsize(self.info_path)
        given_size = int(self.info_size)
        return file_size == given_size

if __name__ == "__main__":
    POSITIVE_TEST = \
            FileChecker('data/omni_20160622-000000-lookup_data.tar.gz', \
            '1b8307f057dbd01be01117f39ffead77', 478)
    if POSITIVE_TEST.test_file_present():
        print "File present"
    else:
        print "File not present - this shouldn't have happened"
    if POSITIVE_TEST.test_md5sum():
        print "Checksum ok"
    else:
        print "Checksum not ok - this shouldn't have happened"
    if POSITIVE_TEST.test_size():
        print "Size ok"
    else:
        print "Size not ok - this shouldn't have happened"

    FILE_NOT_PRESENT_TEST = \
            FileChecker('data/xxomni_20160622-000000-lookup_data.tar.gz', \
            '1b8307f057dbd01be01117f39ffead77', 478)
    if FILE_NOT_PRESENT_TEST.test_file_present():
        print "File present - this should not have happened"
    else:
        print "File not present - this is ok in this test"

    CHECKSUM_NOT_OK_TEST = \
            FileChecker('data/omni_20160622-000000-lookup_data.tar.gz', \
            '1b8307f057dbd01be01117f39ffead78', 478)
    if CHECKSUM_NOT_OK_TEST.test_md5sum():
        print "Checksum ok - this should not have happened"
    else:
        print "Checksum not ok - this is ok in this test"

    SIZE_NOT_OK_TEST = \
            FileChecker('data/omni_20160622-000000-lookup_data.tar.gz', \
            '1b8307f057dbd01be01117f39ffead77', 479)
    if SIZE_NOT_OK_TEST.test_size():
        print "File size ok - this shouldn't have happened"
    else:
        print "Size not ok - this is ok in this test"

