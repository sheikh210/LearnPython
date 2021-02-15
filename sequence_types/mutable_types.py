# Mutable objects can be changed

shopping_list = ['Milk',
        'Cheese',
        'Eggs',
        'Yogurt'
        ]

another_list = shopping_list

print(id(shopping_list))
print(id(another_list))

# When adding items to a list, we can use the augmented assignment operator (+=), but must place the value in []
shopping_list += ['Cookies']
print(shopping_list)

# Same ID as shopping_list, prior to adding "Cookies"
print(id(shopping_list))
# Since we are only using 1 list, another_list will contain "Cookies", as well
print(another_list)

# Another example of line 20 & 21
a = b = c = d = e = f = another_list
print(a)
print("Adding Cream to another_list")
b.append("Cream")
print(c)
print(d)
print("Adding Chicken to another_list")
e.append("Chicken")
print(e)
print(f)