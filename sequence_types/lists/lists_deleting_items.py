# We only want numbers between 100-200 contained in the list

data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]

# del data[:2]
# print(data)
#
# del data[14:]
# print(data)

min_valid = 100
max_valid = 200

# # ***THIS WILL NOT WORK - ONCE A VALUE GETS DELETED, THE INDEXES CHANGE
# for index, value in enumerate(data):
#     if (value < min_valid) or (value > max_valid):
#         del data[index]
#         # index -= 1 - THIS WILL NOT WORK AS THE VALUE OF INDEX IS RESET EACH ITERATION OF THE LOOP

# HOW TO SAFELY DELETE FROM AN ORDERED LIST
# 1. Process low values in the ordered list
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print(stop) # For debugging
del data[:stop]
print(data)

# 2. Process the high values in the ordered list
start = 0
max_range = len(data) - 1
             # range of list|stop|step
for index in range(max_range, -1, -1):
    if data[index] <= max_valid:
        start = index + 1
        break

print(start) # For debugging
del data[start:]
print(data)