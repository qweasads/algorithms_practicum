def fib(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]

    fib_sequence = [0, 1]
    for i in range(2, n + 1):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    return fib_sequence

def fib_sequence():
    test_values = [8, 10, 15, 20]
    for n in test_values:
        result = fib(n)
        print(f"fib({n}) = {result}")

if __name__ == "__main__":
    fib_sequence()