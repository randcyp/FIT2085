# Great discussion about shoving metadata into people's faces:
# https://stackoverflow.com/questions/1523427/what-is-the-common-header-format-of-python-files

# FIT2085 requires two main elements to be present before import statements
# """Docstring module as an overview of the file"""
# __author__ variable that indicates the author

# https://docs.python.org/3/library/typing.html#typing.TypeVar
# Can't really find comprehensive information on TypeVar

from typing import TypeVar

T = TypeVar("T", int, str)


def get_element(x: int, y: int):
    a = [0, 1, 2, 0, 1, 2, 0, 1, 2]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    c = "Almost done!"
    d = [a, b, c]

    return d[x][y]


print("get_element(0, 4): " + str(get_element(0, 4)))
print("get_element(1, 9): " + str(get_element(1, 9)))
print("get_element(2, -1): " + str(get_element(2, -1)))
