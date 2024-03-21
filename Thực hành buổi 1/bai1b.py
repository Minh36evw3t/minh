def Fibonacci_iterative(n):
    if n <= 1:
        return n
    else:
        fib_sequence = [0, 1]
        for i in range(2, n + 1):
            fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
        return fib_sequence[n]


def main_iterative():
    n = int(input("Nhập số nguyên n: "))
    if n < 0:
        print("Nhập số nguyên không âm.")
    else:
        print("Số Fibonacci thứ", n, "là:", Fibonacci_iterative(n))

main_iterative()
