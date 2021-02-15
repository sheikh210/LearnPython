shopping_cart = []
choice = '-'

computer_parts_list = ['pc',
                       'monitor',
                       'mouse',
                       'graphics card',
                       'hdmi cable'
                       ]

valid_choices = [str(i) for i in range(1, len(computer_parts_list) + 1)]

while choice != "0":

    if choice in valid_choices:
        item = computer_parts_list[int(choice) - 1]
        print("\nAdded {} to shopping list\n".format(item))
        print('-' * 10)
        shopping_cart.append(item)
    else:
        print("WHICH ITEM WOULD YOU LIKE TO ADD TO SHOPPING CART?")

        # This is logical, but Python has a built-in enumerate() function, which makes this easier
        # for i in range(len(computer_parts_list)):
        #     print("{}\t".format(i + 1) + computer_parts_list[i])

        # enumerate() function returns a pair of values - the index, and the item at that index
        # This is why we can use 2 variables in the for-each loop declaration (number, part)
        # We can use enumerate() with any iterable-type (refer to enumerate_practice.py)
        for number, part in enumerate(computer_parts_list):
            print("{}\t{}".format(number + 1, part))

    choice = input("MAKE YOUR SELECTION: ")

print('-' * 25)
print("\nSHOPPING LIST:\t")
print(shopping_cart)
