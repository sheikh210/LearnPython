# age = int(input("PLEASE ENTER AGE: "))

# if age >= 18 and age <= 65: (same as below)
# if 18 <= age <= 65:
#     print("Adult")


# day = "Saturday"
# temp = 30
# raining = True
#
# if day == "Saturday" and temp > 27 and not raining:
#     print("Go Swimming")
# else:
#     print("Learn Python")

# TRUTHY VALUES
if 0:
    print("TRUE")  # THIS LINE IS UNREACHABLE DUE TO 0 ALWAYS REPRESENTING FALSE
else:
    print("FALSE")

name = input("PLEASE ENTER YOUR NAME: ")

# if name != "":
if name:
    print("Hello, {}!".format(name))
else:
    print("Do you not have a name?")
