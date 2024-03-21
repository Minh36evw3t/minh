def GCD_iterative(m, n):
    while n != 0:
        m, n = n, m % n
    return m


def main_iterative():
    m = int(input("Nhập số nguyên dương thứ nhất m: "))
    n = int(input("Nhập số nguyên dương thứ hai n: "))
    if m <= 0 or n <= 0:
        print("Nhập hai số nguyên dương.")
    else:
        print("Ước số chung lớn nhất của", m, "và", n, "là:", GCD_iterative(m, n))


main_iterative()
