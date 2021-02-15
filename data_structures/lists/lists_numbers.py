even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# extend() method adds the parameter (odd) to the object (even)
even.extend(odd)
print("even.extend(odd)")
print(even)

# sort() method doesn't create a new list, rather rearranges the items in the list - Sorts the list "in place"
another_even_list = even
print("another_even_list")
print(another_even_list)

even.sort()
print("even.sort()")
print(even)

even.sort(reverse=True)
print("even.sort(reverse=True)")
print(even)

print("another_even_list")
print(another_even_list)


#
# print()
#
# print("mississippi".count("s"))
# print("mississippi".count("iss"))
#
# # Output of this is 1, because Python doesn't re-use the 'i' b/w the 2 pairs of S's
# print("mississippi".count("issi"))
