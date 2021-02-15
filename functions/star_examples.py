numbers = (1, 2, 3, 4, 5)


# Using * unpacks the sequence (tuple in this example)
# The first print statement won't print any separators, as it is only 1 value
#    This ensures that Python is, in fact, unpacking our sequence type, then printing it as separate values
print(numbers, sep=";")
print(*numbers, sep=";")
print(1, 2, 3, 4, 5, sep=";")

print('\n' + "-" * 25 + '\n')


# We can also use * the other way around - pass in 'n' number of arguments to a function
# In this example, *args will unpack all the arguments passed into the function
# Printing 'args' will give us the tuple, while iterating over args, prints each argument individually
def test_star(*args):
    print(args)

    for x in args:
        print(x)


test_star(1, 2, 3, 4, 5)

# We can also pass no arguments to our function, as seen below - The output produces an empty tuple
# More importantly, our function didn't crash
print()
test_star()
