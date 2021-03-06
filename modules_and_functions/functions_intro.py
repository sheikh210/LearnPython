# # Functions must always be defined with keyword 'def', followed by function name and :
# def python_food():
#     print('Spam & Eggs')
#
#
# # Calling the function
# python_food()
#
# # All Python functions return a result. If no return is defined, then the function returns None by default
# print(python_food())
#
#
# # ***Parameterized functions***
# def center_text(text):
#     width = 80
#     left_margin = width - len(text) // 2
#     print(' ' * left_margin, text)
#
#
# center_text('We Are')
# center_text('Centering')
# center_text('The Text That We Pass')
# center_text('As An Argument To The center_text() Function')
#
# # If we pass numerical value to the center_text() function, we will be thrown an error (len() doesn't exist for numbers)
# # center_text(10)
#
# # We can fix this by accepting *args (any number of args) and casting the arg to str using the str()
#
#
# def center_text(*args):
#     text = ''
#     for arg in args:
#         text += str(arg) + ' '
#     left_margin = 80 - len(text) // 2
#     print(' ' * left_margin, text)
#
#
# center_text('Sami', 210, 'Aamna', 407)


# We can accept any number of keyword arguments using the following:
def save_user(**user):
    print(f"User ID: {user['id']}\nFirst Name: {user['first_name']}\nLast Name: {user['last_name']}")


# Calling this function will return a dict
save_user(id=1, first_name="Sami", last_name="Sheikh")
