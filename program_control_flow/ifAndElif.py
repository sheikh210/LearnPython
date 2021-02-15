# name = input('ENTER YOUR NAME: ')
# age = int(input('ENTER YOUR AGE, {0}: '.format(name)))
#
# print(age)
#
# if age < 21:
#     print("YOU WILL BE ELIGIBLE TO VOTE IN {} YEARS".format(21-age))
# elif age >= 100:
#     print("PLEASE CALL 555-555-5555 TO DETERMINE ELIGIBILITY")
# else:
#     print("YOU ARE ELIGIBLE TO VOTE")

answer = 5

print("GUESS A NUMBER BETWEEN 1 AND 10")
guess = int(input())

# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("CORRECT!!!")
#     else:
#         print("Please try again")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("CORRECT!!!")
#     else:
#         print("Please try again")
# else:
#     print("CORRECT!!!")

if guess != answer:
    if guess > answer:
        print("Please guess lower")
    else:
        print("Please guess higher")
    guess = int(input())
    if guess == answer:
        print("CORRECT!!!")
    else:
        print("PLEASE TRY AGAIN :(")
else:
    print("CORRECT!!! FIRST TRY!")