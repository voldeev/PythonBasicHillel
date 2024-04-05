import string

letters = input("Введіть дві літери через дефіс: ")
start, end = letters.split('-')
result = ''
start_index = string.ascii_letters.index(start)
end_index = string.ascii_letters.index(end)
for i in range(start_index, end_index + 1):
    result += string.ascii_letters[i]

print(result)
