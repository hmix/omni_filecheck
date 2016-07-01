import os
import re
from itertools import islice
from fileinfo import *
from filechecker import *

class CheckFile:

    def __init__(self, file_path, metadata=[], fileinfo=[]):
        self.file_path = file_path
        self.file_name = os.path.basename(file_path)
        self.metadata=[]
        self.fileinfo = []

    # Remove whitespace / empty lines
    def clean_checkfile(self):
        file_handler = open(self.file_path)
        filtered = filter(lambda x: not re.match(r'^\s*$', x), file_handler)
        return filtered

    # The first four lines of a omniture checkfile is metadata
    def set_metadata(self):
        head = self.clean_checkfile()
        head = head[:4]
        for line in head:
            # print(line)
            self.metadata.append(line)

    # A fileinfo dataset consists of three lines of information
    # The first four lines are metadata and must be removed
    def set_fileinfo(self):
        body = self.clean_checkfile()
        body_fileinfo = body[4:]
        # Create list with groups of three elements
        body_fileinfo_structured = map(None, *(iter(body_fileinfo),) * 3)
        # Create fileinfo objects and append them to instance
        for element in body_fileinfo_structured:
            file_type = element[0].split(':')[0].strip()
            file_name = element[0].split(':')[1].strip()
            file_checksum = element[1].split(':')[1].strip()
            file_size = element[2].split(':')[1].strip()
            file_info = FileInfo(file_type, file_name, file_checksum, file_size)
            self.fileinfo.append(file_info)


if __name__ == "__main__":
    test = CheckFile('data/omni_file_checkfile.txt')
    test.set_metadata()
    print("Header:")
    print test.metadata
    test.set_fileinfo()
    print("Fileinfo:")
    # print test.fileinfo
    for f_info in test.fileinfo:
        print f_info.file_type
        print f_info.file_name
        print f_info.file_checksum
        print f_info.file_size

        fc = FileChecker('data/' + f_info.file_name, f_info.file_checksum, str(f_info.file_size))
        if fc.test_file_present():
            print "File present - ok"
        else:
            print "Error: File not found " + fc.info_path
        if fc.test_md5sum():
            print "Checksum ok"
        else:
            print "Checksum not ok"
        if fc.test_size():
            print "Size ok"
        else:
            print "Size not ok"

    # Check file acording to fileinfo
    # Is file present?
    # Is file size correct?
    # Is checksum correct?
