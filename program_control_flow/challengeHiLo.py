import random

low = 1
high = 1000
answer = random.randint(1, 1000)

print("ANSWER: {}".format(answer))

numOfGuesses = 1

while True:
    guess = low + (high - low) // 2

    if guess < answer:
        low = guess + 1
    elif guess > answer:
        high = guess - 1
    elif guess == answer:
        guessCorrect = True
        print("CORRECT ANSWER: {}\n\tNUMBER OF GUESSES: {}".format(guess, numOfGuesses))
        break

    numOfGuesses += 1
