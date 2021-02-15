# Assign default values to parameters with the assignment operator (=)
def sum_even_odd(n: int = 0, t: str = "e") -> int:
    calc = 0

    if t == "e":
        for i in range(0, n):
            if i % 2 == 0:
                calc += i
    elif t == "o":
        for i in range(1, n, 2):
            if i % 2 != 0:
                calc += i
    else:
        return -1

    return calc


print(sum_even_odd())

# When passing just 1 argument to this function, we have to define which parameter the argument will be assigned to
#   This is called a keyword argument
print(sum_even_odd(n=20))
