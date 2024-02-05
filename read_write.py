"""Text file reader class"""
import os
import sys
from pathlib import Path


class FileNameError(Exception):
    pass


class FileExtensionError(Exception):
    pass


class TextFileReader:
    """TextFileReader class
        Attributes:
            - file_name
            - file_path
        Methods: size, get_content
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


class TextFileWriter:
    """TextFileWriter class
        Attributes:
            - file_name
            - file_path
        Methods:
    """
    def __init__(self, file_name):
        """Initialize objects"""

        p = Path(__file__)
        self.file_name = file_name
        if not isinstance(self.file_name, str):
            raise FileNameError('File name must be of type str!')
        if os.path.splitext(self.file_name)[1] != '.txt':
            raise FileExtensionError('File extension must be .txt!')

        self.file_path = str(p.parent / self.file_name)

    def write_to_file(self, data: str, mode='w'):
        """Write data to file
        """
        if not isinstance(data, str):
            raise ValueError('Input data must be of type str!')

        with open(self.file_name, mode) as fw:
            fw.write(f'{data}\n')


if __name__ == "__main__":
    try:
        text_file = TextFileWriter('dummy_file.txt')
        text_file.write_to_file('Crina are mere!')
    except FileNameError as e:
        print('wrong name!')
        print(e)
    except FileExtensionError:
        print('wrong file extension')

