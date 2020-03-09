# Part A

# Notes for this exercise
# List comprehension reading:
# https://stackoverflow.com/questions/3013449/list-comprehension-vs-lambda-filter


def print_intersection(list1, list2):
    return [x for x in list1 if x in list2]


print("print_intersection([2, 4, 8], [9, 2, 3]): "
      + str(print_intersection([2, 4, 8], [9, 2, 3])))