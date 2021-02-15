# We can coerce (cast) an int into a string using the str operator (not efficient)
age = 30
print("My age is " + str(age) + " years")

# Using the .format function, we can pass in the values of our variables to the string literal using indexes
age2 = 31
print("My age is {0} years. I will be {1} years old next month".format(age, age2))

print()

print("JAN: {2}, FEB: {0}, MAR: {2}, APR: {1}, MAY: {2}, JUN: {1}, JUL: {2}, AUG: {2}, SEP: {1}, OCT: {2}, NOV: {1}, DEC: {2}".format(28, 30, 31))

print()

print("""JAN: {2} {3}
FEB: {0} {3}
MAR: {2} {3}
APR: {1} {3}
MAY: {2} {3}
JUN: {1} {3}
JUL: {2} {3}
AUG: {2} {3}
SEP: {1} {3}
OCT: {2} {3}
NOV: {1} {3}
DEC: {2} {3}""".format(28, 30, 31, "Days"))