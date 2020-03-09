# Notes for this exercise
# Use the '//' operand for division ignoring decimal points


def string_to_hex(string):
    base10_num = int(string)
    remainders = []

    while base10_num != 0:
        remainders.append(base10_num % 16)
        base10_num //= 16

    base16_str = ""
    for x in reversed(remainders):
        if x > 9:
            base16_str += ["A", "B", "C", "D", "E", "F"][x-10]
        else:
            base16_str += str(x)

    return base16_str


print("string_to_hex(1128): " + string_to_hex(1128))
print("string_to_hex(118): " + string_to_hex(188))
