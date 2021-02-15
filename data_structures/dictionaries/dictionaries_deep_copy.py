# To use deep copy, we need to import the copy module to our python file
import copy

# DEEP COPY - Copies literals of mutable objects, not references (like shallow copy)

animals = {"lion": ["scary", "big", "cat"],
           "elephant": ["big", "friendly", "gray"],
           "teddy": ["cuddly", "plush", "stuffed"],
           }

# Creating a deep copy
things = copy.deepcopy(animals)

print(animals["teddy"])
print(things["teddy"])
print()

# Append to things["teddy"]
things["teddy"].append("toy")

# Output is different, as things["teddy"] and animals["teddy"] are 2 different lists, as seen by different id's
print(id(animals["teddy"]), animals["teddy"], sep=" - ")
print(id(things["teddy"]), things["teddy"], sep=" - ")
print()
