#Варіант з використанням операторів
a = int(input("Введіть 4-х значне число: "))
print(a // 1000)
print((a // 100) % 10)
print((a // 10) % 10)
print((a // 1) % 10)

#Варіант з використанням функції divmode
b = int(input("Введіть 4-х значне число: "))
с, b = divmod(b, 1000)
print(с)
с, b = divmod(b, 100)
print(с)
с, b = divmod(b, 10)
print(с)
print(b)
