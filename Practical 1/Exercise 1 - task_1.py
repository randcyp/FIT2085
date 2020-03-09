# Non-assessed practical

"""
This module demonstrates a way to interface basic list
operations.
"""

__author__ = "Chia Yong Peng"

from typing import List, TypeVar

T = TypeVar('T')
list_of_items = []


def print_menu() -> None:
    """
    Prints the menu.
    """
    menu_items = ["append", "reverse", "print", "pop", "count", "quit"]
    print("Menu: ")
    for i in range(0, len(menu_items)):
        print(str(i+1) + ". " + menu_items[i])
    print()


def reverse(ls: List[T]) -> List[T]:
    """
    Reverses a list.
    :param ls: The list to be reversed
    :return: The reversed list
    """

    for i in range(len(ls) // 2):
        ls[i], ls[len(ls) - 1 - i] = ls[len(ls) - 1 - i], ls[i]

    return ls


def count(ls: List[T], obj: T) -> int:
    """
    Returns the number of times an element appears in a list
    :param ls: The list to iterate through
    :param obj: The element to be counted
    :return: The number of times an element appears in a list
    """
    return len([x for x in ls if x is obj])


# Displays the menu and prompts for an option
while True:
    print_menu()
    option = int(input("Enter an option: "))

    if option == 1:
        item = input("Enter an item: ")
        list_of_items.append(item)
    elif option == 2:
        reverse(list_of_items)
    elif option == 3:
        print(list_of_items)
    elif option == 4:
        print(list_of_items.pop())
    elif option == 5:
        item = input("Enter an item: ")
        print(count(list_of_items, item))
    elif option == 6:
        exit()
    else:
        print("You've entered an invalid option, please try again.")

    print()

