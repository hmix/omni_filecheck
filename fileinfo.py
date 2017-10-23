# -*- coding: utf-8 -*-


class FileInfo:
    """
    Representation of file information.
    """

    def __init__(self, file_type, file_name, file_checksum, file_size=0,
                 file_record_count=0):
        self.file_type = file_type
        self.file_name = file_name
        self.file_checksum = file_checksum
        self.file_size = file_size
        self.file_record_count = file_record_count
