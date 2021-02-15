# Write a function that returns the next answer in a game of Fizz Buzz
# You start counting, in turn. If the number is divisible by 3, you say "fizz" instead of the number
# If the number if divisible by 5, you say "buzz" instead of the number
# If the number is divisible by 3 & 5, you say "fizz buzz" instead of the number
# The function should return the correct word ("fizz", "buzz" or "fizz buzz"), or the number if not
#       divisible by 3 or 5
# The function will always return a string
#
# Include a for loop to test your function for values from 1-100, inclusive

def fizz_buzz(number: int) -> str:
    """
    Function to return "fizz" if param `number` is divisible by 3 and not divisible by 5.
    Function to return "buzz" if param `number` is divisible by 5 and not divisible by 3.
    Function to return "fizz buzz" if param `number` is divisible by 3 and divisible by 5.
    Else function returns number
    :param number: Number to be checked if divisible by 3 and/or 5
    :return: "fizz", "buzz", "fizz buzz" or number passed as argument
    """

    if number % 15 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)


# PLAY FIZZ BUZZ AGAINST THE COMPUTER!
for i in range(1, 101):
    if i % 2 != 0:
        print(fizz_buzz(i))
    else:
        user_input = str(input())

        if user_input != fizz_buzz(i):
            print("YOU LOSE!")
            break
else:
    print("WELL DONE, YOU REACHED 100!")
    