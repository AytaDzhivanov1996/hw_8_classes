import os


class ChangeDir:
    def __init__(self, dir_name):
        self.dir_name = dir_name

    def __enter__(self):
        os.chdir(self.dir_name)

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir('../')


with ChangeDir('dir1'):
    print(os.listdir())

with ChangeDir('dir2'):
    print(os.listdir())
