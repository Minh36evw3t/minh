def GCD_recursive(m, n):
    if n == 0:
        return m
    else:
        return GCD_recursive(n, m % n)


def main_recursive():
    m = int(input("Nhập số nguyên dương thứ nhất m: "))
    n = int(input("Nhập số nguyên dương thứ hai n: "))
    if m <= 0 or n <= 0:
        print("Nhập hai số nguyên dương.")
    else:
        print("Ước số chung lớn nhất của", m, "và", n, "là:", GCD_recursive(m, n))


main_recursive()
