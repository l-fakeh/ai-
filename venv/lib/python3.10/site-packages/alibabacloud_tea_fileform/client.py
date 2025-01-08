import random

from alibabacloud_tea_fileform.file_form import FileFormInputStream


class Client:
    @staticmethod
    def get_boundary():
        result = '%s' % int(random.random() * 100000000000000)
        return result.zfill(14)

    @staticmethod
    def to_file_form(form, boundary):
        return FileFormInputStream(form, boundary)
