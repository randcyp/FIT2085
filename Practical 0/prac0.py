# Non-assessed practical

__author__ = "Chia Yong Peng"


# Typing non-primitive types require importing
from typing import List


# Exercise 2
def read_integers() -> List[int]:
    """
    Prompts the user to input a list of integers
    seperated by spaces.

    :return: A list of integers
    """
    list_string = input("Enter some integers: ")

    if len(list_string) == 0:
        return []
    else:
        return [int(x) for x in list_string.split(" ")]


print(read_integers())
print(read_integers())
print(read_integers())


# Exercise 3
def sum_squared_integers(int_list: List[int]) -> int:
    """
    Takes a list of integers and squares it.

    :param int_list: A list of integers
    :return: A list of squared integers
    """
    return sum([x ** 2 for x in int_list])


print("sum_squared_integers([]): ", + sum_squared_integers([]))
print("sum_squared_integers([-6]): ", + sum_squared_integers([-6]))
print("sum_squared_integers([1, -2, 6, 0]): ", + sum_squared_integers([1, -2, 6, 0]))


# Exercise 4
def read_from_file_sum_squares():
    """
    Prompts for a filename of a text file with integers and
    displays the sum of squares of each line.
    """
    # Good refernce for file I/O:
    # https://www.tutorialspoint.com/python/python_files_io.htm
    # Using default 'r' read-only mode

    file = open(input("Enter the filename: "))
    lines = file.read().split("\n")
    sum_of_squares = []

    for line in lines:
        if len(line) == 0:
            # If the line is empty, append a 0
            sum_of_squares.append(0)
        else:
            # If the line has integers, append the sum of squares
            sum_of_squares.append(sum([int(x) ** 2 for x in line.split(" ")]))

    for line in sum_of_squares:
        print(line)


read_from_file_sum_squares()
read_from_file_sum_squares()


# Exercise 5
def read_from_file_table():
    """
    Prompts for a filename of a text file with integers
    stores the non-negative integers in lists.
    """

    file = open(input("Enter the filename: "))
    lines = file.read().split("\n")
    int_list = []

    for line in lines:
        if len(line) == 0:
            # If the line is empty, append a 0
            int_list.append([])
        else:
            # If the line has integers, append the non-negative integers
            int_list.append([int(x) for x in line.split(" ") if x.find("-") == -1])

    print(int_list)


read_from_file_table()
read_from_file_table()