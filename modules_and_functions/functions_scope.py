message = 'a'


def greet():
    message = 'b'


greet()
print(message)  # Will print the value of the global variable


# We can re-assign the value of a global variable inside of a function, HOWEVER THIS IS EXTREMELY BAD PRACTICE
message_2 = 'a'


def greet_2():
    global message_2  # YOU SHOULD NEVER DO THIS
    message_2 = 'b'


greet_2()
print(message_2)
