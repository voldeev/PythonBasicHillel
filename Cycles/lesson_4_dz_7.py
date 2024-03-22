input_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
# input_list_2 = [0]
# input_list_3 = [1, 0, 13, 0, 0, 0, 5]
# input_list_4 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

i = len(input_list) - 1
while i >= 0:
    if input_list[i] == 0:
        input_list.append(input_list.pop(i))
    i -= 1

print(input_list)
