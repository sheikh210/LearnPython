# HOW TO SAFELY DELETE FROM AN UN-ORDERED LIST (Iterate over it backwards)
# This works for ordered & un-ordered lists

data = [104, 101, 4, 105, 308, 103, 5,
        107, 100, 306, 106, 102, 108]

min_valid = 100
max_valid = 200

# for index in range(len(data) - 1, -1, -1):
#     if (data[index] > max_valid) or (data[index] < min_valid):
#         print(index, data)
#         del data[index]
#
# print(data)

# Much more efficient way to perform the above operation is to use reversed() function - returns reverse iterator

top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        del data[top_index - index]
        print(top_index - index, value)

print(data)