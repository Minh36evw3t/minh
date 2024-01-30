def Dao_nguoc_so_nguyen(number):
   
    str_number = str(number)
    
    if str_number[0] == '-':
        reversed_str = '-' + str_number[:0:-1]
    else:
        reversed_str = str_number[::-1]

    Dao_nguoc_so_nguyen = int(reversed_str)

    return Dao_nguoc_so_nguyen

input_number = int(input("Nhập giá trị: "))
result = Dao_nguoc_so_nguyen(input_number)
print(f"Giá trị đảo ngược là: {result}")
