def is_palindrome(s):

    cleaned_string = ''.join(s.split()).lower()
    
    return cleaned_string == cleaned_string[::-1]

input_string = input("Nhập chuỗi: ")
if is_palindrome(input_string):
    print("Chuỗi đã nhập là một chuỗi palindrome.")
else:
    print("Chuỗi đã nhập không phải là chuỗi palindrome.")
