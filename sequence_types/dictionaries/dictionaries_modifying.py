fruit = {"orange": "A sweet orange citrus fruit",
         "apple": "Good for making cider",
         "lemon": "A sour, yellow citrus fruit",
         "grape": "A small, sweet fruit grown in bunches",
         "lime": "A sour, green citrus fruit",
         }

# ADDING ITEMS TO DICTIONARIES
fruit["pear"] = "An odd-shaped apple"
print(fruit["pear"])
print()

# RE-ASSIGNING KEY VALUES
fruit["pear"] = "A very thicc fruit"
print(fruit["pear"])
print()

# DELETING ITEMS FROM DICTIONARIES
# Method 1 - del
print(fruit)
del fruit["pear"]
print(fruit)
print()

# Method 2 - pop()
# **IMPORTANT: Deleting an item using a key that doesn't exist, will crash the program. You can pass None as an argument
#              to the pop() method, that way it doesn't crash and returns the value that is passed, instead.
#              Sometimes, however, we want our code to crash.
print(fruit)
# fruit.pop("watermelon")
result = fruit.pop("watermelon", None)
print(result)
print()

# CLEARING A DICTIONARY
fruit.clear()
print(fruit)
print()

# DELETING WHOLE DICTIONARIES
del fruit


# The values in our dictionary don't have to be of the same type. The keys must be of an immutable type (no lists)

motorcycle = {"manufacturer": "Honda",
              "make": "250 Dream",
              "color": "Black",
              "engine_size": 250,
              }
