letters = 'abcdefghijklmnopqrstuvwxyz'

backwards = letters[25::-1]
print(backwards)

# Output is same as above
# Python is smart enough to know we want the entire string reversed, simply by using -1 step value
backwards2 = letters[::-1]
print(backwards2)

# CHALLENGE
# Create a slice that prints 'qpo'
# Create a slice that prints 'edcba'
# Create a slice that prints the last 8 characters in reverse order

print()

print(letters[16:13:-1])
print(letters[4::-1])
print(letters[:-9:-1])

print("\nPRINTING LAST & FIRST INDEXES USING SLICE")
print(letters[-1:])
print(letters[:1])


# We can print the first index using letters[0], however this will produce a run-time error if string is empty
print('\nTHIS IS THE FIRST LETTER: ' + letters[:1])



