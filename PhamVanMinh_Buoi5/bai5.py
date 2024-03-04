def count_word_frequency(words):
    word_frequency = {}
    for words in words:
        if words in word_frequency :
            word_frequency[words] += 1
        else:
            word_frequency[words] = 1
    for words, count in word_frequency .items():
        print(f'{words}: {count}')
# Ví dụ sử dụng
words = ['nhap', 'xuat', 'nhap', 'nhap', ]
count_word_frequency(words)