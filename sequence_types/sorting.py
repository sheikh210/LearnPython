# sorted() function can be used to sort any iterable - sorted() returns a NEW sorted list

pangram = "The quick brown fox jumps over the lazy dog"

# key is another argument that can be passed to sorted() function or sort() method
letter = sorted(pangram, key=str.casefold)

print(letter)

print()

# ***IMPORTANT: sorted() function returns an entirely different list
# ***IMPORTANT: sort() method reorganizes the same list and returns None
number = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(number)

print(sorted_numbers)

another_sorted_numbers = number.sort()
print(another_sorted_numbers) # Returns None

print()

missing_letter = sorted("The quick brown fox jumped over the lazy dog", key=str.casefold)
print(missing_letter)

print()

names = ["Graham",
         "John",
         "terry",
         "eric",
         "Terry",
         "michael"
         ]

names.sort(key=str.casefold)
print(names)