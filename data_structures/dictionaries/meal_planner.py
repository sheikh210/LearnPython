from data_structures.dictionaries.dictionaries_meals import pantry, recipes

# Dictionary Comprehension (At the time of writing this, I need to understand this code better)
# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}


def add_item(our_shopping_list: dict, item: str, quantity: int) -> None:    # Function to add items to shopping list
    # if item in our_shopping_list:
    #     our_shopping_list[item] += quantity
    # else:
    #     our_shopping_list[item] = quantity
    our_shopping_list[item] = our_shopping_list.setdefault(item, 0) + quantity  # Python way of writing lines 8-11


# Create an empty dict - Line 15-20 is the longer way to perform code on line 4
display_dict = {}

# Use the enumerate function to create indexes for the keys in the recipes dict
for index, key in enumerate(recipes):
    # Add to the empty display_dict ('index + 1' becomes the key, and 'key' becomes the value)
    display_dict[str(index + 1)] = key

shopping_list = {}

while True:
    print("PLEASE CHOOSE YOUR RECIPE:")
    print('-' * 25)

    for key, value in display_dict.items():
        print(f"{key} - {value}")

    choice = input("\nMAKE YOUR SELECTION: ")

    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"YOU HAVE SELECTED {selected_item}. THIS RECIPE CALLS FOR:")
        ingredients = recipes[selected_item]
        print(ingredients)

        for ingredient, required_qty in ingredients.items():
            if ingredient not in pantry:
                print(f"\tYou need to go get {required_qty} of {ingredient}. Added {ingredient} to your shopping list")
                add_item(shopping_list, ingredient, required_qty)

            elif ingredient in pantry:
                pantry_qty = pantry.get(ingredient)

                if required_qty > pantry_qty:
                    diff = required_qty - pantry_qty
                    print(f"\tYou are short {diff} {ingredient}. Added to your shopping list")
                    add_item(shopping_list, ingredient, diff)

                elif required_qty <= pantry_qty:
                    print(f"\tYou have enough {ingredient} - {pantry_qty} in pantry")

for things, qty in shopping_list.items():
    print(things, qty, sep=": ")
