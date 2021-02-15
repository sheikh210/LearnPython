# Python 3 has 5 different sequence types (A sequence is an ordered set of items):
# string
# list
# tuple
# range
# byte & bytearray

# Because a sequence is ordered, we can use indexes to access individual items in the sequence

string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords"

print(string1 + string2 + string3 + string4 + string5)

# We can concatenate without using the "+" operator
print("he's " "probably " "pining " "for the " "fjords")
# Using commas adds a space between strings automatically
print(string1, string2, string3, string4, string5)


# We can multiply strings - This will print (or perform whatever operation on) the string n number of times
print("Hello " * 5)

# This throws an error - Order of precedence + we can't concat an int to a string
# print("Hello " * 5 + 4)

print("Hello " * 5 + "4")

# How to check if a sequence exists within another sequence
today = "friday"
# Evaluates to True
print("day" in today)
print("fri" in today)
# Evaluates to False
print("thur" in today)
print("parrot" in "fjord")
