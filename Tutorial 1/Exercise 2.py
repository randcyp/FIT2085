def is_palindrome(string):
    return string == string[::-1]


words = ["ab3ba", "ab3bbaba", "321236"]

for x in words:
    print(x + ": " + str(is_palindrome(x)))
