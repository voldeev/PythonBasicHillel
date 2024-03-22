input_list = [0, 1, 7, 2, 4, 8]

if not input_list:
    result = 0
else:
    sum_even_indices = sum(input_list[i] for i in range(0, len(input_list), 2))
    last_element = input_list[-1]
    result = sum_even_indices * last_element

print(result)
