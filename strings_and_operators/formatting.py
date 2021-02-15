# This is the exponent operator: **
# Using :2 or :4 after the index allows us format the output by determining width of field
for i in range(1,13):
    print("NUMBER: {0:2} NUMBER SQUARED: {1:3} NUMBER CUBED: {2:4}".format(i, i**2, i**3))

print()

# To left align, use the < operator after the colon, but before the width value
# To right align use the > operator after the colon, however right align is done by default
# To center align, use the ^ operator
for i in range(1,13):
    print("NUMBER: {0:<2} NUMBER SQUARED: {1:<3} NUMBER CUBED: {2:<4}".format(i, i**2, i**3))

print()

for i in range(1,13):
    print("NUMBER: {0:^2} NUMBER SQUARED: {1:^3} NUMBER CUBED: {2:^4}".format(i, i**2, i**3))

print()

# Floating point precision (Maximum of 51-53 floating point digits)

# The default value of floating point precision is 15 digits (in the 2nd example, the 12 width value is
# overridden by Python's default floating point precision of 15.
print("Pi is approx. {0}".format(22/7))
print("Pi is approx. {0:12}".format(22/7))

# When we declare an 'f' after the width value, then Python prints the default value of 6 floating point precision,
# but maintains the width of 12 for the output, hence why it appears to be formatted with an indent.
print("Pi is approx. {0:12f}".format(22/7))

# We can also declare the width of the floating point precision by declaring .precisionValue + f after the width value.
# In this first example, we can't print a value having 50 floating point precision with width value of 12, so Python
# automatically overrides the width by the declared floating point value and prints with a 50 floating point precision.
print("Pi is approx. {0:12.50f}".format(22/7))

# The following 3 examples print 50 floating point values, with corresponding widths
print("Pi is approx. {0:52.50f}".format(22/7))
print("Pi is approx. {0:62.50f}".format(22/7))
print("Pi is approx. {0:<72.50f}".format(22/7))

# The last example demonstrates Python's floating point precision limit, as it appends 0's to the end of the decimal
print("Pi is approx. {0:<72.54f}".format(22/7))

print()

# Printing with .format without specifying index values (cannot re-use values in .format() function, as we're not
# declaring any indexes in the string to be printed.
for i in range(1,13):
    print("NUMBER: {} NUMBER SQUARED: {} NUMBER CUBED: {:4}".format(i, i**2, i**3))