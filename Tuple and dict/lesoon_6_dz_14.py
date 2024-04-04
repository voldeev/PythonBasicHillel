num = int(input("Введіть ціле число: "))

while num >= 10 and num != 0:
    product = 1
    for digit in str(num):
        product *= int(digit)
    num = product
    if num <= 9:
        break

print(num)
