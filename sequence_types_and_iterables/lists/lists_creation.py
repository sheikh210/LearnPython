empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
print(numbers)

# Returns a list of integers
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

# Returns a list of individual strings
digits = sorted("432985617")
print(digits)

# We can create an un-sorted list of individual strings using the list class initializer
digits_list = list("432985617")
print(digits)

# There are various ways to copy lists
more_numbers = list(numbers)
more_numbers_2 = numbers[:]
more_numbers_3 = numbers.copy() # This is the easiest way
