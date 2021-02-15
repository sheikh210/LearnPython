# menu = [
#     ["egg", "bacon"],
#     ["egg", "sausage", "bacon"],
#     ["egg", "spam"],
#     ["egg", "bacon", "spam"],
#     ["egg", "bacon", "sausage", "spam"],
#     ["spam", "bacon", "sausage", "spam"],
#     ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
#     ["spam", "egg", "spam", "spam", "bacon", "spam"],
# ]
#
# for meal in menu:
#     for index in range(len(meal) - 1, -1, -1):
#         if meal[index] == "spam":
#             del meal[index]
#     print(", ".join(meal))


flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger Lily",
]

# for flower in flowers:
#     print(flower)

# join() is a method of the str class - It will work on any iterable
# join() iterates for us
separator = ", "
output = separator.join(flowers)
print(output)
