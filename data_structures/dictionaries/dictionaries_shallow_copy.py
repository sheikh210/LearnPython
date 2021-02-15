animals = {"lion": "scary",
           "elephant": "big",
           "teddy": "cuddly",
           }

animals_list_dict = {"lion": ["scary", "big", "cat"],
                     "elephant": ["big", "friendly", "gray"],
                     "teddy": ["cuddly", "plush", "stuffed"]
                     }

# things = animals
# # `animals` and `things` refer to the same dictionary - proof below
# animals["teddy"] = "toy"
# print(things["teddy"])
# print()
#
# # COMMENT LINES 8-10 BEFORE RUNNING CODE BELOW
# # If we use the .copy method on `animals`, `things_copy` represents a copy of `animals` and not the same dictionary
# things_copy = animals.copy()
# print(things_copy["teddy"])
# print()

# # SHALLOW COPY
# # Shallow copy, copies references to mutable objects in memory, not literals
# # Refer to dictionaries_shallow_copy_2 for remaining explanation
# things_list_dict = animals_list_dict.copy()
# print(animals_list_dict["teddy"])
# print(things_list_dict["teddy"])
# print()
#
# things_list_dict["teddy"].append("toy")
# print(animals_list_dict["teddy"])
# print(things_list_dict["teddy"])
# print()
