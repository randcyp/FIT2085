# Non-assessed practical

"""
This module is an interface for converting
decimals to binary or hexadecimal.
"""

__author__ = "Chia Yong Peng"

from typing import TypeVar

T = TypeVar('T')
list_of_items = []


def print_menu() -> None:
    """
    Prints the menu.
    """
    menu_items = ["Decimal to Binary", "Decimal to Hexadecimal",
                  "Quit"]
    print("Menu: ")
    for i in range(0, len(menu_items)):
        print(str(i+1) + ". " + menu_items[i])
    print()


def dec_to_bin(decimal: int) -> int:
    """
    Converts a decimal integer to binary
    :param decimal: An integer
    :return: A binary number
    """
    remainder_str = ""

    while decimal != 0:
        remainder_str += str(decimal % 2)
        decimal //= 2

    return int(remainder_str[::-1])


def dec_to_hex(decimal: int) -> str:
    """
    Converts a decimal integer to a hexadecimal string
    :param decimal: An integer
    :return: A hexadecimal string
    """
    remainders = []

    while decimal != 0:
        remainders.append(decimal % 16)
        decimal //= 16

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
        integer = int(input("Enter an integer: "))
        print(dec_to_bin(integer))
    elif option == 2:
        integer = int(input("Enter an integer: "))
        print(dec_to_hex(integer))
    elif option == 3:
        quit()
    else:
        print("You've entered an invalid option, please try again.")

    print()

