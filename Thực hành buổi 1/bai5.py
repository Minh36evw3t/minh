def classify_number(n):
    divisor_sum = sum([i for i in range(1, n) if n % i == 0])
    if divisor_sum < n:
        return "deficient"
    elif divisor_sum == n:
        return "perfect"
    else:
        return "abundant"

def Number(x, y):
    if x <= 0 or y <= 0 or x > y:
        print("Nhập hai số nguyên dương hợp lệ (x <= y).")
    else:
        for i in range(x, y + 1):
            print("Số", i, "là", classify_number(i))


def main():
    x = int(input("Nhập số nguyên dương x: "))
    y = int(input("Nhập số nguyên dương y: "))
    Number(x, y)


main()
