first_num = int(input("Введіть перше число: "))
operator = input("Введіть дію (+, -, *, /): ")
second_num = int(input("Введіть дреге число: "))

if operator == '+':
    print("Результат:", first_num + second_num)
elif operator == '-':
    print("Результат:", first_num - second_num)
elif operator == '*':
    print("Результат:", first_num * second_num)
elif operator == '/':
    if second_num != 0:
        print("Результат:", first_num / second_num)
    else:
        print("Ділити на нуль не можна!")
