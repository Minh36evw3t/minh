def are_anagrams(phrase1, phrase2):
    
    cleaned_phrase1 = ''.join(phrase1.split()).lower()
    cleaned_phrase2 = ''.join(phrase2.split()).lower()

    return sorted(cleaned_phrase1) == sorted(cleaned_phrase2)

input_phrase1 = input("Nhập từ hoặc cụm từ thứ 1: ")
input_phrase2 = input("Nhập từ hoặc cụm từ thứ 2: ")

if are_anagrams(input_phrase1, input_phrase2):
    print("Các từ hoặc cụm từ đã nhập là đảo chữ.")
else:
    print("Các từ hoặc cụm từ đã nhập không phải là đảo chữ.")
