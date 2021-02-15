from sequence_types_and_iterables.dictionaries.dictionaries_meals import pantry

# setdefault() returns the value of a key, if the key exists in the dict
# If the key does NOT exist, then it creates the key, with the default value that we pass in setdefault()
chicken_qty = pantry.setdefault("chicken", 0)
print(f"Chicken: {chicken_qty}")

