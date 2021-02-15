def fibonacci(n: int = 1) -> int:
    """
    Calculates & returns the `n` th Fibonacci number, where `n` represents
    a positive integer (indexing starts at 0)
    :param n: Number of Fibonacci iterations
    :return: nth Fibonacci number
    """

    if 0 <= n <= 1:
        return n

    f1, f2 = 0, 1
    f3 = None

    sequence = [f1, f2]

    for f in range(n - 1):
        f3 = f1 + f2
        sequence.append(f3)
        f1 = f2
        f2 = f3

    return f3


for i in range(36):
    print(i, fibonacci(i))

