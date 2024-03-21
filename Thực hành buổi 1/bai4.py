def calculate_pascal_triangle(n):
    pascal_triangle = []
    for i in range(n):
        row = [1]  
        if i > 0:
            for j in range(1, i):
                row.append(pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j])
            row.append(1)  
        pascal_triangle.append(row)
    return pascal_triangle

def print_pascal_triangle(pascal_triangle):
    for i, row in enumerate(pascal_triangle):
        print("n={}".format(i), end=" ")
        for num in row:
            print(num, end=" ")
        print()


def main():
    n = int(input("Nhập số nguyên dương n: "))
    if n <= 0:
        print("Nhập số nguyên dương.")
    else:
        pascal_triangle = calculate_pascal_triangle(n)
        print("Tam giác Pascal ứng với bậc", n, "là:")
        print_pascal_triangle(pascal_triangle)


main()
