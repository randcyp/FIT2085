# Part 1

a_list = [1, 2, 3, 4, 5]
a = a_list[1]
b = a_list[3]

print(a)
print(b)

# Part 2

a_string = "FIT2085"
print(a_string[a])
print(a_string[b])

# Part 3
print("a = not True: " + str(not True))
print("b = 2 + 2 > 4: " + str(2 + 2 > 4))
print("c = not '0' == 0: " + str(not '0' == 0))

# Reassigning variables with non matching type values is possible
d = True
d = []
print("d = " + str(d))

# Converting a blank string to a boolean yields false
print("e = not \"\": " + str(not ""))

# Values that yield 'False' when converted to a boolean
false_values = [0, "", [], None]
for x in false_values:
    print(str(x) + " converted to boolean is: " + str(bool(x)))

print("f = not 2 - len([a, \"potato\")): " + str(not 2 - len([a, "potato"])))
print("g = len(d): " + str(len([])))
print("h = not g: " + str(not 0))
print("i = len(d): " + str(len(['foo'])))
print("j = not 'foo': " + str(not "foo"))
print("k = not 4 % 1: " + str(not 4 % 1))
