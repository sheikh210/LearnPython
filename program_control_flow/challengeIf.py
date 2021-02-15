name = input("What is your name?: ")
age = int(input("How old are you?: "))

if age <18 or age > 31:
    print("Sorry, you must be between 18 and 31 years old to attend")
else:
    print("Welcome aboard, {}!".format(name))