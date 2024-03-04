def check_same_frequency(list1, list2):
    
    frequency_dict = {}
    for item in list1:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    for item in list2:
        if item not in frequency_dict or frequency_dict[item] == 0:
            return False
        frequency_dict[item] = 1
    return all(frequency == 0 for frequency in frequency_dict.values())
list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
result = check_same_frequency(list1, list2)

print(result)