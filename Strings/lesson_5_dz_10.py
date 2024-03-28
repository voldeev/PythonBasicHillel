variable_name = input("Введіть ім'я змінної: ")

if (variable_name[0].isdigit() or any(char.isupper() for char in variable_name) or
    any(char in "+-*/\\=<> !@#$%^&*()[]{}`~|;:'\",.?/" for char in variable_name) or
    '__' in variable_name):
    print(False)
else:
    if variable_name in ['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else',
                         'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
                         'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']:
        print(False)
    else:
        print(True)
