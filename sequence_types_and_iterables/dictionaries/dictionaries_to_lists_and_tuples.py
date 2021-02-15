fruit = {"orange": "A sweet orange citrus fruit",
         "apple": "Good for making cider",
         "lemon": "A sour, yellow citrus fruit",
         "grape": "A small, sweet fruit grown in bunches",
         "lime": "A sour, green citrus fruit",
         }


fruit_list_keys = list(fruit)
print("LIST OF KEYS")
print(fruit_list_keys)
print('-' * 25)

fruit_list_values = list(fruit.values())
print("LIST OF VALUES")
print(fruit_list_values)
print('-' * 25)

fruit_tuple_keys = tuple(fruit)
print("TUPLE OF KEYS")
print(fruit_tuple_keys)
print('-' * 25)

fruit_tuple_values = tuple(fruit.values())
print("TUPLE OF VALUES")
print(fruit_tuple_values)
print('-' * 25)


# We can also use .items() method to get the key-value pairs and place them in a list/tuple

items_list = list(fruit.items())
print("LIST OF ITEMS")
print(items_list)
print('-' * 25)

items_tuple = tuple(fruit.items())
print("TUPLE OF ITEMS")
print(items_tuple)
print('-' * 25)

# We can then unpack the list/tuple
print("UNPACKED TUPLE OF ITEMS")
for snack in items_tuple:
    item, description = snack
    print(item + " is " + description)
print('-' * 25)