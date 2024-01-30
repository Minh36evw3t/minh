def daonguoc_array_in_place(array):
    for i in range(len(array) // 2):
        array[i], array[-i - 1] = array[-i - 1], array[i]

    return array


array = [1, 2, 3, 4, 5]
print(f"Chuỗi đảo ngược là:{daonguoc_array_in_place(array)}")