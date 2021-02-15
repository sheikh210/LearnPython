import random

lower_limit = 1
upper_limit = 10
answer = random.randint(lower_limit, upper_limit)

print("GUESS A NUMBER BETWEEN {}-{}: ".format(lower_limit, upper_limit))
numOfGuesses = 1
guess = 0

while guess != answer:
    guess = int(input("Guess: "))

    if guess < lower_limit or guess > upper_limit:
        print("QUITTING GAME")
        break
    elif guess < answer:
        print("GUESS AGAIN! --- Hint: Go higher\n")
        numOfGuesses += 1
    elif guess > answer:
        print("GUESS AGAIN! --- Hint: Go lower\n")
        numOfGuesses += 1

if guess == answer:
    if numOfGuesses == 1:
        print("CORRECT! YOU GOT IT ON YOUR FIRST TRY!\n\tGUESSED: {} ANSWER: {}".format(guess, answer))
    else:
        print("CORRECT! YOU GOT IT ON TRY #{}\n\tGUESSED: {} ANSWER: {}".format(numOfGuesses, guess, answer))