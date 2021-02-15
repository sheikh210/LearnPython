# Write a functon that takes a dictionary as an argument and returns a deep copy of the dictionary
# Do not import the copy module
# Pretend that any dictionary passed as an argument only contains 1 level of contained objects (lists as values)
# It shouldn't have to handle dictionaries that contain objects, that also contain objects

from data_structures.dictionaries.dictionaries_shallow_copy import animals_list_dict


def create_deep_copy(dict_to_be_copied: dict) -> dict:
    """
    Creates a deep copy of a dict
    :param dict_to_be_copied: Dictionary that will be copied
    :return: Copied dictionary
    """

    empty_dict = {}

    for key, value in dict_to_be_copied.items():
        new_value = value.copy()
        empty_dict[key] = new_value

    return empty_dict


new_dict = create_deep_copy(animals_list_dict)
print(new_dict)

new_dict["lion"] = ["scary", "hairy", "coward"]
print(new_dict["lion"])
print(animals_list_dict["lion"])

