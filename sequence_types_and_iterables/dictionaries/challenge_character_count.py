# Write some code to count the number of times each character occurs in the given `text` string
# Do this for every unique character in the `text` string, ignoring spaces and all other special characters
# When counting the characters, make sure to ignore case ("Be bold" would have a count of 2 for the letter 'b')
# Store the count in the letter_count dictionary, with the key being the character

# We need an empty dictionary, to store and display the letter frequencies.
letter_count = {}

# Text string
text = "Later in the course, you'll see how to use the collections Counter class."

# Your code goes here ...
irrelevant_text = []

for char in text.casefold():
    if char not in 'abcdefghijklmnopqrstuvwxyz':
        irrelevant_text.append(char)

new_text_list = "".join(char if char not in irrelevant_text else "" for char in text.casefold())
print(new_text_list)

for char in new_text_list:
    if char not in letter_count:
        letter_count[char] = 1
    elif char in letter_count:
        letter_count[char] += 1


# Printing the dictionary
for letter, count in sorted(letter_count.items()):
    print(letter, count)

