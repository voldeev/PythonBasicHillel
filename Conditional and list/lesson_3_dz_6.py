input_list = [12, 3, 4, 10]

if len(input_list) > 1:
    # Видаляємо останній елемент зі списку
    last_element = input_list.pop()
    # Вставляємо його на початок списку
    input_list.insert(0, last_element)

print(input_list)