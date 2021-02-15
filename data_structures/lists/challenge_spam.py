# Write code to print out all the meals, but with spam removed
# You can choose which approach to use:
#   1. Remove spam from each list, then print the list
#   2. Print out the items in each list, as long as it's not spam
# BONUS: Write both sets of code

menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

# # Method 1
# for meal in menu:
#     if "spam" not in meal:
#         print(meal)
#     else:
#         top_index = len(meal) - 1
#         for index, value in enumerate(reversed(meal)):
#             if value == "spam":
#                 del meal[top_index - index]
#         print(meal)

# # BETTER WAY TO CODE METHOD 1
# for meal in menu:
#     for index in range(len(meal) - 1, -1, -1):
#         if meal[index] == "spam":
#             del meal[index]
#     print(meal)

# # Method 2
# for meal in menu:
#     for value in meal:
#         new_meal = []
#         if value != "spam":
#             print(value, end=", ")
#     print() # Without this print(), all items would print on the same line

# Method 2 - Without trailing commas (using a generator)
for meal in menu:
    items = ", ".join(item for item in meal if item != "spam")
    print(items)
