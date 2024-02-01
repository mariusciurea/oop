"""Text file reader class"""
import os
import sys
from pathlib import Path


class TextFileReader:
    """TextFileReader class
        Attributes:
            - file_name
            - size
        Methods:
    """

    def __init__(self, file_name):
        p = Path(__file__)
        self.file_name = file_name
        self.file_path = str(p.parent / self.file_name)

    def size(self):
        """Return file size"""
        try:
            return os.path.getsize(self.file_path)
        except FileNotFoundError:
            print(f'Cannot get the size because of the following reason: '
                  f'{self.file_name} does not exist!')
            sys.exit(2)

    def get_content(self):
        """Return file content"""
        try:
            with open(self.file_path, 'r') as f_read:
                content = f_read.read()
                return content
        except FileNotFoundError:
            print(f'Cannot get the content because of the following reason: '
                  f'{self.file_name } does not exist!')
            sys.exit(2)


if __name__ == "__main__":
    text_file = TextFileReader('test.txt')
    print(text_file.file_name)
    print(text_file.file_path)
    print(text_file.size())
    print(text_file.get_content())

    readme = TextFileReader('README1.md')
    print(readme.size())
    print(readme.get_content())
