# Create a multiplication table

for i in range(13):
    print("{} TIMES TABLE:".format(i))
    for j in range(13):
        int = i * j
        print("{} x {} = {}".format(i, j, int))
    print("-" * 25)
