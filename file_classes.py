import os
from io import TextIOWrapper


class FileFinder:
    def __init__(self, suffixes: list[str], find_path):
        self.suffixes = suffixes
        self.find_path = find_path
        self.all_file_names: list[str] = []

    def is_true_suffix(self, file_name):
        file_name_in_list = file_name.split(".")
        suffix = file_name_in_list[len(file_name_in_list) - 1]
        return suffix in self.suffixes

    def find_all_all_file_with_true_suffixes(self):
        all_file_names = os.listdir(self.find_path)
        print(all_file_names)
        for file_name in all_file_names:
            if self.is_true_suffix(file_name):
                self.all_file_names.append(file_name)


class FileEditor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.file: TextIOWrapper | None = None
        self.file_text = ""

    def open_file(self):
        self.file = open(self.file_path, "r+")

    def close_file(self):
        self.file.close()

    def read_file(self):
        self.file_text = self.file.read()

    def replace_data_in_file(self, string_for_replace: str, new_string: str):
        new_text = self.file_text.replace(string_for_replace, new_string)
        self.file.write(new_text)
        self.file_text = new_text