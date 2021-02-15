shopping_list = ['Milk', 'Cat Food', 'Eggs', 'Bagels', 'Yogurt', 'Sponges', "Toilet Paper"]

item_to_find = 'Bagels'
foundAt = None

# NOT AN EFFICIENT WAY TO LOOP THROUGH THE LIST
# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         foundAt = index + 1
#         break
if item_to_find in shopping_list:
    foundAt = shopping_list.index(item_to_find) + 1

if foundAt is not None:
    print("{} IS ITEM #{} IN THE LIST".format(item_to_find.upper(), foundAt))
else:
    print("ITEM NOT FOUND")
