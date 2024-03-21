input_list = [1, 2, 3, 4, 5, 6]
# input_list_2 = [1, 2, 3]
# input_list_3 = [1, 2, 3, 4, 5]
# input_list_4 = [1]
# input_list_5 = []

first_list = input_list[:len(input_list) // 2 + len(input_list) % 2]
second_list = input_list[len(input_list) // 2 + len(input_list) % 2:]

result = [first_list, second_list]

print(result)
