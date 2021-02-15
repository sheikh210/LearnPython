parrot = "Norwegian Blue"

letter = input("ENTER A CHARACTER: ")

# if letter in parrot:
#     print("{} is in {}".format(letter, parrot))
# else:
#     print("I don't need that letter")


# The .casefold() function returns a version of the string/character suitable for caseless comparisons
if letter.casefold() not in parrot:
    print("I don't need that letter")
else:
    print("{} is in {}".format(letter, parrot))