# Non-assessed practical

__author__ = "Chia Yong Peng"

from typing import List
import random

# Stores the first puzzle state
puzzle = [[0 for i in range(4)] for j in range(4)]

# A dictionary for retrieving the right increments for a particular direction
DIRECTION_INCREMENTS = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}

# Stores tuples of every move made by the player
# Format: [(square number, direction), (...)]
move_stack = []

# Stores the current puzzle state
puzzle_state = [[0 for a in range(4)] for b in range(4)]


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

    # Append the sequence to the puzzle & puzzle state
    for i in range(4):
        for j in range(4):
            square = random_puzzle.pop()
            puzzle[i][j] = square
            puzzle_state[i][j] = square


def get_index(square_num: int) -> List[int]:
    """
    Gets the indices of a square given the square number

    :param square_num: An integer representing a square
    :return: Returns a union with 2 indices
    """

    for i in range(4):
        for j in range(4):
            if puzzle_state[i][j] == square_num:
                return [i, j]


def get_space_index() -> List[int]:
    """
    Gets the indices of space.
    :return: The space indices in a list. [row_index, col_index]
    """
    for i in range(4):
        for j in range(4):
            if not puzzle_state[i][j]:
                return [i, j]


def display_puzzle():
    """
    Displays the current state of the puzzle
    """

    print()

    for row in puzzle_state:
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
            adj_square = puzzle_state[adj_row][adj_col]

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


def prompt_move():
    """
    Prompts the user for a valid move.
    """
    while True:
        # Display the puzzle
        display_puzzle()

        # Display the menu

        # {square_num, direction}
        possible_moves = get_possible_moves()

        print("Possible moves: ")

        for square in possible_moves.keys():
            print("Square " + str(square) + ", " + str(possible_moves[square]).capitalize())

        option = input("\nPlease choose a square"
                       "\n('q' to quit, 'b' to undo move): ").strip().lower()

        if option == 'q':
            quit()
        elif option == 'b':
            # Back (Undo move)

            if len(move_stack) > 0:
                # If moves are made, undo the most previous move
                move_stack.pop()
            else:
                # If moves are not made, show an error
                print("There are no previous moves.")
            break
        elif option.isdigit():
            # Add a move to the move stack

            square = int(option)
            if square in possible_moves.keys():
                move = (square, possible_moves[square])
                move_stack.append(move)
                break
            else:
                print("Square number invalid, please try again.")
        else:
            print("Invalid option, please try again.")


def update_puzzle():
    """
    Modifies the puzzle board based on the move stack.
    """
    # Reset the puzzle to its first state
    for i in range(4):
        for j in range(4):
            puzzle_state[i][j] = puzzle[i][j]

    # Make every move in the move stack
    for move in move_stack:
        # Get the indices of the exchanging pieces
        square_index = get_index(move[0])

        row = square_index[0]
        new_row = row + DIRECTION_INCREMENTS[move[1]][0]

        col = square_index[1]
        new_col = col + DIRECTION_INCREMENTS[move[1]][1]

        # Swap them
        puzzle_state[row][col], puzzle_state[new_row][new_col] =\
            puzzle_state[new_row][new_col], puzzle_state[row][col]


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
                if puzzle_state[i][j] != current_square:
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
        prompt_move()
        update_puzzle()

    print("We have a winner!")


start()
