# UNION - Joins 2 sets, omitting repeated values
# **********************************************************************************************************************
even_numbers = set(range(0, 40, 2))
print(even_numbers)
print(len(even_numbers))
print('*' * 25)

squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(squares)
print(len(squares))
print('*' * 25)

print(even_numbers.union(squares))
print(len(even_numbers.union(squares)))
print('*' * 25)

# INTERSECTION - Values shared by 2 sets (Line 20-23 are the different ways of writing the same thing
# **********************************************************************************************************************
print(even_numbers.intersection(squares))
print(even_numbers & squares)
print('*' * 10)
print(squares.intersection(even_numbers))
print(squares & even_numbers)
print('*' * 25)

# DIFFERENCE - Returns a new set containing values not shared by one set, when compared against another set
# **********************************************************************************************************************
print(even_numbers.difference(squares))
print(even_numbers - squares)
print('*' * 10)
print(squares.difference(even_numbers))
print(squares - even_numbers)
print('*' * 25)

# DIFFERENCE_EVEN - Modifies a set in place (returns None), omitting values shared by 2 sets
# **********************************************************************************************************************
print(even_numbers.difference_update(squares))  # Returns None
print(even_numbers)
print('*' * 10)
print(squares.difference_update(even_numbers))  # Returns None
print(squares)
print('*' * 25)

# SYMMETRIC_DIFFERENCE
# **********************************************************************************************************************
print(even_numbers.symmetric_difference(squares))
print(squares.symmetric_difference(even_numbers))
print('*' * 25)



