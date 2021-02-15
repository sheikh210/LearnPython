import random


def get_user_input_integer(prompt: str = "Enter number:") -> int:
    """
    Get an `int` value from stdin.
    The function will continue looping & prompting the user until a valid `int` is entered
    :param prompt: String displayed to user when prompting for input
    :return: Integer entered by user
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)

        print("{} isn't a valid number".format(temp))


low_value = 1
high_value = 1000
answer = random.randint(low_value, high_value)
print(answer)   # For debug

guess = 0

print("Please guess a number between {} & {}".format(low_value, high_value))

while guess != answer:
    guess = get_user_input_integer()

    if guess == 0:
        break
    if guess == answer:
        print("CORRECT!!!")
    else:
        if guess > answer:
            print("GUESS LOWER")
        else:
            print("GUESS HIGHER")
