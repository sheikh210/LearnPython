fruit = {"orange": "A sweet orange citrus fruit",
         "apple": "Good for making cider",
         "lemon": "A sour, yellow citrus fruit",
         "grape": "A small, sweet fruit grown in bunches",
         "lime": "A sour, green citrus fruit",
         }

while True:
    dict_key = input("Which fruit would you like the description of?: ").casefold()

    if dict_key == "quit":
        break
    elif dict_key == "" or dict_key == " ":
        continue
    description = fruit.get(dict_key, "Sorry, we don't have any {}".format(dict_key))
    print(description)
