# SHALLOW COPY (Continued from dictionaries_shallow_copy)

lion_list = ["scary", "big", "cat"]
elephant_list = ["big", "friendly", "gray"]
teddy_list = ["cuddly", "plush", "stuffed"]

# Values stored in the dictionary are not lists - they are references to lists, even when we pass literals to the dicts
# (Explicitly demonstrated below)
animals_list_dict = {"lion": lion_list,
                     "elephant": elephant_list,
                     "teddy": teddy_list
                     }

# The reason why .copy() method makes both values for ["teddy] refer to the same list, is because the lists are actually
# just a reference to the lists in memory
things_list_dict = animals_list_dict.copy()
print(animals_list_dict["teddy"])
print(things_list_dict["teddy"])
print()

# When we append "toy" to "teddy", the list gets updated, however both `things_list_dict` and `animals_list_dict`
# reference the same exact list
things_list_dict["teddy"].append("toy")
print(animals_list_dict["teddy"])
print(things_list_dict["teddy"])
print()

# To labor the point, we update "teddy" from 2 different references, and print out all 3 of the references
animals_list_dict["teddy"].append("Added via `animals_list_dict")
things_list_dict["teddy"].append("Added via `things_list_dict")

# These will all print the same list
print(animals_list_dict["teddy"])
print(things_list_dict["teddy"])
print(teddy_list)
