panagram = "The quick brown fox jumps over the lazy dog"

words = panagram.split()
print(words)

numbers = "9, 223, 372, 036, 854, 775, 807"

separators = ""

for char in numbers:
    if char not in "0123456789":
        separators += char

# .split() returns a list
numbers_list = "".join(char if char not in separators else "" for char in numbers).split()
print(numbers_list)

# Add a space in the else clause to return a list of multiple strings
numbers_list_2 = "".join(char if char not in separators else " " for char in numbers).split()
print(numbers_list_2)

# Without using .split(), we get a string
numbers_string = "".join(char if char not in separators else "" for char in numbers)
print(numbers_string)

# MINI-CHALLENGE
#   1. Use a for-loop to produce a list of ints, rather than strings (use numbers_list_2)
#   2. You can either modify the contents of 'numbers_list_2' list in place or create a new list of ints

# Method 1 - Replace the values in place
for index in range(len(numbers_list_2)):
    numbers_list_2[index] = int(numbers_list_2[index])

print(numbers_list_2)

# Method 2 - Create a new list (First we need to create our starting list of strings,
# so we cannot use 'numbers_list_2' again since it was already converted to list of ints
numbers_list_3 = "".join(char if char not in separators else " " for char in numbers).split()
new_list = []

for value in numbers_list_3:
    new_list.append(int(value))

print(new_list)
