import time

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

def fib_execution_timer():
    test_values = [5, 10, 15, 20, 24]
    for n in test_values:
        start_time = time.time()
        result = fib(n)
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000
        print(f"fib({n}) = {result}, время выполнения: {execution_time:.2f} мс")

if __name__ == "__main__":
    fib_execution_timer()