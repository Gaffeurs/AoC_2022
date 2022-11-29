import os
import glob
import shutil


def create_directories():
    for i in range(2, 26):
        os.mkdir(rf".\day_{i:02d}")


def copy_jupyter():
    for path_directory in glob.glob("./day*")[1:]:
        shutil.copy(r".\day_01\day_01.ipynb", rf"{path_directory}{path_directory[1:]}.ipynb")


def create_readme():
    for i in range(1, 26):
        with open(rf".\day_{i:02d}\README.md", 'w') as f:
            f.write(f"JOUR {i:02d}")


if __name__ == '__main__':
    create_directories()
    copy_jupyter()
    create_readme()
