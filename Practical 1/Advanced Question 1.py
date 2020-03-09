# Non-assessed practical

__author__ = "Chia Yong Peng"

from typing import List

puzzle = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, None]]


def getIndex(square_num: int) -> List[int]:
    """
    Gets the indices of a square given the square number

    :param square_num: An integer representing a square
    :return: Returns a union with 2 indices
    """

    for i in range(4):
        for j in range(4):
            if puzzle[i][j] == square_num:
                return [i, j]


def displayPuzzle():
    """
    Displays the current state of the puzzle
    """

    for row in puzzle:
        line = ""
        for column in row:
            if column:
                line += "%3d" % column
            else:
                line += "   "
        print(line)


while True:
    print()
    displayPuzzle()
    option = input("Choose a square ('q' to quit): ").strip()

    if option.isdigit():
        square = int(option)

        if square not in range(1, 16):
            print("Invalid square number, numbers can only range from 1 to 16.")
        else:
            # square_index = [row_index, col_index]
            square_index = getIndex(square)
            row = square_index[0]
            col = square_index[1]

            # A dictionary for retrieving the right increments for a particular direction
            dirIncrement = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}

            direction = input("Choose a direction (up, down, left or right): ").strip().lower()
            if direction not in dirIncrement.keys():
                print("Invalid direction, please try again.")
                continue

            new_row = row + dirIncrement[direction][0]
            new_col = col + dirIncrement[direction][1]

            # Check if the new position is empty (e.g. None)
            if not puzzle[new_row][new_col]:
                # Empty
                puzzle[new_row][new_col] = puzzle[row][col]
                puzzle[row][col] = None
            else:
                print("There is no space, please try again.")
                # Not Empty
    else:
        if option.lower() == "q":
            quit()
        else:
            print("Invalid option, please try again.")

