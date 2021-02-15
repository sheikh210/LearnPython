# Dictionaries are items in key-value pairs (like a hash-map in Java)
# Dictionaries and Sets are NOT sequence types, hence we can't call values using indexes

fruit = {"orange": "A sweet orange citrus fruit",
         "apple": "Good for making cider",
         "lemon": "A sour, yellow citrus fruit",
         "grape": "A small, sweet fruit grown in bunches",
         "lime": "A sour, green citrus fruit",
         }

print(fruit)
print()

# Accessing dictionary items using their key - We can use the normal [] way, or we can use the dictionary built-in
# function, called .get() to retrieve the value of that particular key
# **IMPORTANT - Using the .get() function will return 'None' if key doesn't exist. Using [] will crash the program if
#               the key doesn't exist. Indexing, however, is faster when retrieving values
print(fruit["orange"])
print(fruit["apple"])
print(fruit.get("lemon"))
print(fruit.get("grape"))
print(fruit.get("lime"))
print()