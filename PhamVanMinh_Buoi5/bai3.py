def filter_dict(input_dict, condition):
    filtered_dict = {}
    
    for key, value in input_dict.items():
       
        if condition(key, value):
            filtered_dict[key] = value
    return filtered_dict
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filter_dict = filter_dict(my_dict, lambda k, v: v % 2 == 0)
print(filter_dict)