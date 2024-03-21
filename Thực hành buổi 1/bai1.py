def Fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return Fibonacci_recursive(n-1) + Fibonacci_recursive(n-2)


def main_recursive():
    n = int(input("Nhập số nguyên n: "))
    if n < 0:
        print("Nhập số nguyên không âm.")
    else:
        print("Số Fibonacci thứ", n, "là:", Fibonacci_recursive(n))


main_recursive()
