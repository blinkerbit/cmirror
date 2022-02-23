# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os.path
import sys
import argparse
from pathlib import Path
import distutils.spawn


def mirror():
    new_name =sys.argv[1]
    print(sys.argv)
    if sys.argv[2].strip() != "=":
        raise Exception("incorrect format ")
    old_name = sys.argv[3]
    path= Path(distutils.spawn.find_executable('mirror'))
    print(path)
    file = path.parent / f"{new_name}.bat"
    with file.open("w") as f:
        f.write(f'{old_name} %* ')




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
