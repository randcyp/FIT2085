# Non-assessed practical

__author__ = "Chia Yong Peng"

from typing import List, Tuple
import random

# Placeholder puzzle
puzzle = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, None]]

# A dictionary for retrieving the right increments for a particular direction
DIRECTION_INCREMENTS = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}


def init_puzzle():
    """Initializes the puzzle with a random one."""
    # Random puzzle sequence
    random_puzzle = []

    while len(random_puzzle) != 16:
        random_square = random.randint(0, 15)

        # If the square does not already exist in the puzzle, add it
        if random_puzzle.count(random_square) == 0:
            random_puzzle.append(random_square)

    # Change square 0 to None
    random_puzzle[random_puzzle.index(0)] = None

    # Append the sequence to the puzzle
    for i in range(4):
        for j in range(4):
            puzzle[i][j] = random_puzzle.pop()


def get_index(square_num: int) -> List[int]:
    """
    Gets the indices of a square given the square number

    :param square_num: An integer representing a square
    :return: Returns a union with 2 indices
    """

    for i in range(4):
        for j in range(4):
            if puzzle[i][j] == square_num:
                return [i, j]


def get_space_index() -> List[int]:
    """
    Gets the indices of space.
    :return: The space indices in a list. [row_index, col_index]
    """
    for i in range(4):
        for j in range(4):
            if not puzzle[i][j]:
                return [i, j]


def display_puzzle():
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

    print()


def get_possible_moves() -> dict:
    """
    Gets the possible moves for the puzzle
    :return: A set of moves in a dictionary. {{square_number: direction}, {...}}
    """
    space_indices = get_space_index()
    space_row = space_indices[0]
    space_col = space_indices[1]

    # Search the adjacent positions of space for adjacent squares
    possible_moves = dict()
    for dir_key in DIRECTION_INCREMENTS.keys():
        adj_row = space_row + DIRECTION_INCREMENTS[dir_key][0]
        adj_col = space_col + DIRECTION_INCREMENTS[dir_key][1]

        if adj_row in range(4) and adj_col in range(4):
            adj_square = puzzle[adj_row][adj_col]

            # dir_key stores the direction as viewed from the space,
            # so we need to invert the direction
            if dir_key == "left":
                possible_moves[adj_square] = "right"
            elif dir_key == "right":
                possible_moves[adj_square] = "left"
            elif dir_key == "up":
                possible_moves[adj_square] = "down"
            else:
                # dir_key == "down"
                possible_moves[adj_square] = "up"
    return possible_moves


def prompt_move() -> Tuple:
    """
    Prompts the user for a valid move.

    :return: A tuple for the move. (square number, direction)
    """
    while True:
        display_puzzle()

        # {square_num, direction|
        possible_moves = get_possible_moves()

        print("Possible moves: ")

        for square in possible_moves.keys():
            print("Square " + str(square) + ", " + str(possible_moves[square]).capitalize())

        option = input("\nPlease choose a square ('q' to quit): ").strip()

        if option.lower() == 'q':
            quit()
        elif option.isdigit():
            square = int(option)

            if square in possible_moves.keys():
                return square, possible_moves[square]
            else:
                print("Square number invalid, please try again.")
        else:
            print("Invalid option, please try again.")


def make_move(move: Tuple):
    """
    Modifies the puzzle board based on a move tuple.

    :param move: A move tuple (Square num, direction)
    """

    # Get the indices of the exchanging pieces
    square_index = get_index(move[0])

    row = square_index[0]
    new_row = row + DIRECTION_INCREMENTS[move[1]][0]

    col = square_index[1]
    new_col = col + DIRECTION_INCREMENTS[move[1]][1]

    # Swap them
    puzzle[row][col], puzzle[new_row][new_col] = puzzle[new_row][new_col], puzzle[row][col]


def is_sorted() -> bool:
    """
    Checks if the puzzle is sorted

    :return: True for sorted, false otherwise.
    """

    current_square = 1

    for i in range(4):
        for j in range(4):
            if not (i == 3 and j == 3):
                # Check for square arrangement excluding the last piece
                if puzzle[i][j] != current_square:
                    return False
                else:
                    current_square += 1
    return True


# Partially sorted puzzle for debugging
# puzzle = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, None, 15]]


def start():
    """Starts the puzzle game"""
    init_puzzle()

    while not is_sorted():
        move = prompt_move()
        make_move(move)

    print("We have a winner!")


start()
