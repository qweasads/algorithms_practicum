import math

def fib(n):
    sqrt_5 = math.sqrt(5)
    phi = (1 + sqrt_5) / 2
    psi = (1 - sqrt_5) / 2

    fib_n = (phi**n - psi**n) / sqrt_5
    return round(fib_n)

def binet_results():
    test_values = [32]
    for n in test_values:
        result = fib(n)
        print(f"fib({n}) = {result}")

if __name__ == "__main__":
    binet_results()