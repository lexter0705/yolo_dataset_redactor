import os
from file_classes import FileFinder, FileEditor


class MarkupReplacer(FileEditor):
    def __init__(self, markup_name: str, markup_path):
        super().__init__(f"{markup_path}/{markup_name}")
        self.open_file()
        self.read_file()