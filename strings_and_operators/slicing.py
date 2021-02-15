parrot = 'Norwegian Blue'

# Slicing requires 3 index values: start, stop, step (default value = 1)

# Norweg - The stop value (6) is non-inclusive
print(parrot[0:6])

# we
print(parrot[3:5])

# Norwegian
print(parrot[0:9])
print(parrot[:9])

# Blue
print(parrot[10:14])
print(parrot[10:])

# Norweg
print(parrot[:6])
print(parrot[6:])

# Norwegian Blue
print(parrot[:6] + parrot[6:])
print(parrot[:])

print('\nUSING STEP')
print(parrot[:6:2])
print(parrot[:6:3])

print('\nSLICE EVERY n CHARACTER')
number = '9-234:562;910_083`849-482.291/236'

seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])
