# Tuples differ from lists, in that they are immutable
# You're still able to perform sequence operators, such as join(), split(), etc

# Good practice is to always use parenthesis when declaring tuples, as there are certain instances where you MUST
#   e.g. - When passing a tuple literal to print(), you must use () within the print() to output a tuple
# t = ('a', 'b', 'c')
# print(t) == print(('a', 'b', 'c'))

welcome = ("Welcome to my nightmare", "Alice Cooper", 1975)
bad = ("Bad Company", "Bad Company", 1974)
budgie = ("Nightflight", "Budgie", 1981)
imelda = ("More Mayhem", "Emilda May", 2011)
metallica = ("Ride the Lightning", "Metallica", 1984)

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

# TUPLES DO NOT SUPPORT ITEM ASSIGNMENT
# metallica[0] = "Master of Puppets"

# Reason to use a tuple over a list
#   1. They don't have the overhead of methods needed to change them = less memory
#   2. Data integrity - tuples are immutable
#   3. You can always unpack a tuple successfully since they are immutable

# Converting a tuple to a list
metallica_2 = list(metallica)
print(metallica_2)
