# Write a function to calc the sum of all numbers passed as its arguments
# The function should be called sum_numbers and take a single argument: the value to sum up to
# The parameters and return value must be annotated (refer to PEP 484)


def sum_numbers(*numbers: float) -> float:
    """
    Calculates the sum of all the numbers passed as arguments
    :param numbers: Numbers to be summed
    :return: Sum of numbers passed as arguments
    """
    result = 0

    for number in numbers:
        result += number

    return result

    # USING BUILT-INS, WE CAN SIMPLIFY TO 1 LINE OF CODE
    # return sum(values)


print(sum_numbers(1, 2, 3))
print(sum_numbers(8, 20, 2))
print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(1.1, 2.2, 5.5))
