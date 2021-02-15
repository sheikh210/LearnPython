parrot = "Norwegian Blue"

# Similar for for-each loop in Java - Define the variable (character) contained within the iterable object (parrot)
# for character in parrot:
#     print(character)

# value = "9,342;534,029 134-390]619"
# separators = ""
#
# for char in value:
#     if not char.isnumeric():
#         separators = separators + char
#
# print(separators)

# Similar to regular for-loops in java - Define a range and iterate n number of times
for i in range(1, 20):
    print("i is {}".format(i))


# If you just want the loop to run n number of times, don't give a start value
for i in range(10):
    print("Aamna & Sami")

# If you'd like to step a distinct amount through the loop, you can provide a step value that is smaller than the
# stop value, but you also have to include the start value
for i in range(0, 10, 2):
    print("Sami & Aamna")
