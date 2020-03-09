# Non-assessed practical

"""
This module is an interface for converting
base 10 decimals to any base.
"""

__author__ = "Chia Yong Peng"

from typing import TypeVar

T = TypeVar('T')
list_of_items = []


def print_menu() -> None:
    """
    Prints the menu.
    """
    menu_items = ["Convert Decimal to Other Base",
                  "Quit"]
    print("Menu: ")
    for i in range(0, len(menu_items)):
        print(str(i+1) + ". " + menu_items[i])
    print()


def simple_conversion(decimal: int, base: int) -> int:
    """
    Converts a decimal integer to bases less than 11
    :param decimal: An integer
    :param base: The base to convert to
    :return: An integer of the specified base
    """
    remainder_str = ""

    while decimal != 0:
        remainder_str += str(decimal % base)
        decimal //= base

    return int(remainder_str[::-1])


def complex_conversion(decimal: int, base: int) -> str:
    """
    Converts a decimal integer to bases more than 11
    :param decimal: An integer
    :param base: The base to convert to
    :return: The converted number in the form of a string
    """
    remainders = []

    while decimal != 0:
        remainders.append(decimal % base)
        decimal //= base

    base16_str = ""
    for x in reversed(remainders):
        if x > 9:
            base16_str += ["A", "B", "C", "D", "E", "F"][x-10]
        else:
            base16_str += str(x)

    return base16_str


# Displays the menu and prompts for an option
while True:
    print_menu()
    option = int(input("Enter an option: "))

    if option == 1:
        number = int(input("Enter an integer: "))
        base = int(input("Enter a base: "))

        if base in range(2, 11):
            print(simple_conversion(number, base))
        elif base in range(11, 17):
            print(complex_conversion(number, base))
        else:
            print("Bases must be within 2 to 16.")
    elif option == 2:
        quit()
    else:
        print("You've entered an invalid option, please try again.")

    print()

