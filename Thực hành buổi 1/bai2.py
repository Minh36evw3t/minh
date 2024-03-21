import math

def Neper(n):
    if n < 0:
        return "Vui lòng nhập số nguyên không âm."
    else:
        e_sum = 0
        for k in range(n + 1):
            e_sum += 1 / math.factorial(k)
        return e_sum

# Hàm chính để test
def main():
    n = int(input("Nhập vào số nguyên n: "))
    print("Tổng của các số hạng từ a0 đến a", n, "là:", Neper(n))

# Gọi hàm chính
main()
