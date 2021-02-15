fruit = {"orange": "A sweet orange citrus fruit",
         "apple": "Good for making cider",
         "lemon": "A sour, yellow citrus fruit",
         "grape": "A small, sweet fruit grown in bunches",
         "lime": "A sour, green citrus fruit",
         }

for snack in fruit:
    print(snack, fruit[snack], sep=": ")

print()

for snack, description in fruit.items():
    print(snack, description, sep=": ")

