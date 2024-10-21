import os
from io import TextIOWrapper


class FileFinder:
    def __init__(self, suffixes: list[str], find_path: str):
        self.__suffixes = suffixes
        self.__find_path = find_path
        self.__all_file_names: list[str] = []

    def __is_true_suffix(self, file_name):
        file_name_in_list = file_name.split(".")
        suffix = file_name_in_list[len(file_name_in_list) - 1]
        return suffix in self.__suffixes

    def find_all_all_file_with_true_suffixes(self):
        all_file_names = os.listdir(self.__find_path)
        for file_name in all_file_names:
            if self.__is_true_suffix(file_name):
                self.__all_file_names.append(file_name)


class FileEditor:
    def __init__(self, file_path: str):
        self.__file_path = file_path
        self.__file: TextIOWrapper | None = None
        self.__file_text = ""

    def open_file(self):
        self.__file = open(self.__file_path, "r+")

    def close_file(self):
        self.__file.close()

    def read_file(self):
        self.__file_text = self.__file.read()

    def replace_data_in_file(self, string_for_replace: str, new_string: str):
        new_text = self.__file_text.replace(string_for_replace, new_string)
        self.__file.write(new_text)
        self.__file_text = new_text