total_seconds = int(input("Введіть кількість секунд (більше або дорівнює 0 і менше ніж 8640000): "))

days, remaining_seconds = divmod(total_seconds, 24 * 60 * 60)
hours, remaining_seconds = divmod(remaining_seconds, 60 * 60)
minutes, seconds = divmod(remaining_seconds, 60)

if days == 1:
    days_word = "день"
elif days % 10 == 1 and days % 100 != 11:
    days_word = "день"
elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20):
    days_word = "дні"
else:
    days_word = "днів"

output = f"{days} {days_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
print(output)
