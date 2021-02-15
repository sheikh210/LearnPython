import random


def high_low_game(answer: int, low: int, high: int) -> int:
    """
    Allows user to define a range of number `low` and `high` and assigns
    a random number within that range as an answer. Function will guess the
    answer in `n` number of guesses
    :param answer: Correct answer that needs to be guessed by function
    :param low: Low value of range
    :param high: High value of range
    :return: Number of guesses required to arrive at answer
    """

    num_of_guesses = 1

    while True:
        guess = low + (high - low) // 2

        if guess < answer:
            low = guess + 1
        elif guess > answer:
            high = guess - 1
        elif guess == answer:
            break

        num_of_guesses += 1

    return num_of_guesses


LOW = 1
HIGH = 1000
correct_count = 0
max_guesses = 0

for number in range(LOW, HIGH + 1):
    number_of_guesses = high_low_game(number, LOW, HIGH)
    print("Answer was {}\n\tTook {} guesses".format(number, number_of_guesses))

    if number_of_guesses > max_guesses:
        max_guesses, correct_count = number_of_guesses, 1
    elif number_of_guesses == max_guesses:
        correct_count += 1

print("\nI guessed without being told {} times. Max {} guesses"
      .format(correct_count, max_guesses))
