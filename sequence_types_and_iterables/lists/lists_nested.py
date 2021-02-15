empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# This concatenates the 2 lists
# numbers = even + odd

# This will create a nested (2d) list
numbers = (even, odd)
print(numbers)

for number_list in numbers:
    print(number_list)

    for value in number_list:
        print(value)
