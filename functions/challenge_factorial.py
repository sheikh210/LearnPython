# A factorial of a number is the product of all values from 1 to the number, inclusive
#   (e.g. - 4! can be written as  4 * 3 * 2 * 1 = 24)
# The convention is that 0! = 1, not 0 as you might expect
# Write a function called factorial that will return the factorial of a number passed as its argument
# Use a for loop to call your factorial function and print out the first 36 (0-35) factorials


def factorial(number: int) -> str:
    """
    Returns the factorial of `number` passed as argument
    :param number: Number to get factorial of
    :return: Factorial of param `number`, as a string
    """

    if number == 0:
        return "1"
    else:
        product = 1
        for count in range(1, number + 1):
            product *= count

    return str(product)


for i in range(0, 36):
    print(i, factorial(i))
