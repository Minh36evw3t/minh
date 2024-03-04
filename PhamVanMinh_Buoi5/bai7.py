def sum_product(input_tuple):
    sum_result = sum(input_tuple)
    product_result = 1
    for num in input_tuple:
        product_result *= num
    result = sum_result * product_result
    return sum_result, product_result, result
input_tuple = (1,3,6,7)
sum_result, product_result, result = sum_product(input_tuple)
print("Tổng:", sum_result)
print("Tích:", product_result)