# Sets are unordered and DO NOT contain any duplicate values - Think of sets like a collection of dictionary keys
# Elements in a set MUST be immutable (hashable)

# DEFINING A SET
# **********************************************************************************************************************
# Method 1 - Declaring a set literal
farm_animals = {'sheep', 'cow', 'hen'}

for animal in farm_animals:
    print(animal)
print('*' * 25)

# Method 2 - Passing a tuple literal to the set() constructor
wild_animals = set(['lion', 'tiger', 'panther', 'elephant', 'hare'])

for animal in wild_animals:
    print(animal)
print('*' * 25)

# Method 2.1 - Passing a tuple variable to the set() constructor
squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(squares)
print('*' * 25)

# Method 2.2 - Passing a range to the set() constructor
even = set(range(0, 40, 2))
print(even)
print('*' * 25)

# ADDING TO A SET
# **********************************************************************************************************************
farm_animals.add('horse')
wild_animals.add('horse')

print(farm_animals)
print(wild_animals)
print('*' * 25)

# REMOVING FROM A SET
# **********************************************************************************************************************
# discard() - Doesn't throw error
farm_animals.discard('horse')
print(farm_animals)

# remove() - Throws exception if value doesn't exist
wild_animals.remove('horse')
print(wild_animals)
print('*' * 25)

