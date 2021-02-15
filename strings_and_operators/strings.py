# print('\'We can use single quotes to surround a string literal\'')
# print("\"Or we can use double quotes\"")
# print("We can also con" + 'catenate strings' + " like this", '....Or like this')
#
# greeting = 'Hello'
# name = input('Please enter your name: ')
#
# print(greeting + ' ' + name + '!')
#
# brokenString = 'This string\nis broken\nup over\nseveral\nlines'
# print(brokenString)
#
# brokenString2 = """Using triple quotes,
# we don't need to insert
# newline characters
# to indent our strings"""
# print(brokenString2)
#
#
# brokenString3 = """However, we can make \
# the string literal \
# look broken \
# but print on a single line \
# using the escape \
# character at the end \
# of each line"""
# print(brokenString3)

name = 'Sami'
age = "thirty"
print(name + ' is ' + age + ' years old')

# THIS WILL THROW AN ERROR (Cannot concat str with int in python)
age = 30
# print(name + ' is ' + age + ' years old.')

# We can convert it to an f-string to include the integer in the string literal
print(name + f' is {age} years old')

print(f'Pi is approx {22/7:12.50f}')

pi = 22/7
print(f'Pi is approx {pi:.50f}')