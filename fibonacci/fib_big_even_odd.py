def fib_eo(n):

    if n == 0:
        return "even"
    elif n == 1:
        return "odd"

    a, b = 0, 1

    for _ in range(2, n + 1):
        a, b = b, (a + b) % 10

    return "even" if b % 2 == 0 else "odd"

if __name__ == "__main__":
    n = int(input("Введите число n: "))
    print(f"Число ({n}) является: {fib_eo(n)}")