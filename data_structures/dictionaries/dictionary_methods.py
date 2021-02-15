d = {0: "zero",
     1: "one",
     2: "two",
     3: "three",
     4: "four",
     5: "five",
     6: "six",
     7: "seven",
     8: "eight",
     9: "nine",
     }

d2 = {
    7: "lucky seven",
    10: "ten",
    3: "this is the new three",
}

pantry = ['chicken', 'spam', 'eggs', 'bread', 'lemon']

# KEYS() METHOD
# **********************************************************************************************************************
# When iterating over a dictionary's keys, it's best practice to utilize the .keys() method to be explicit
for item in d:
    print(item)
print()

for item in d.keys():
    print(item)
print()

# VALUES() METHOD
# **********************************************************************************************************************
# d_values is a "view object" - View Objects are a dynamic view of entries, which are immutable
d_values = d.values()
print(d_values)
print()

# Adding k-v pair in the original dictionary will alter `d_values` to reflect the update
d[10] = "ten"
print(d_values)
print()

print("four" in d_values)
print("eleven" in d_values)
print()

# FROMKEYS() METHOD
# **********************************************************************************************************************
# dict is the class name, and fromkeys() is a class method that generates a new dictionary, with the keys being the
# values contained in the iterable that is passed as an argument to the fromkeys() method
new_dict = dict.fromkeys(pantry)
print(new_dict)
print()

# To assign values to the keys, we can pass an argument defining what the default values should be
new_dict_with_values = dict.fromkeys(pantry, 0)
print(new_dict_with_values)
print()

# UPDATE() METHOD
# **********************************************************************************************************************
# Used to update one dictionary using the contents of another
d.update(d2)
for key, value in d.items():
    print(key, value, sep=": ")
print()

# We can also use the enumerate function to turn the `pantry` list into a dictionary with indexes as the keys
d.update(enumerate(pantry))

for key, value in d.items():
    print(key, value, sep=": ")
print()
