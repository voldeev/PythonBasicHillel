total_seconds = int(input("Введіть кількість секунд (більше або дорівнює 0 і менше ніж 8640000): "))

days, remaining_seconds = divmod(total_seconds, 24 * 60 * 60)
hours, remaining_seconds = divmod(remaining_seconds, 60 * 60)
minutes, seconds = divmod(remaining_seconds, 60)

output = f"{days} днів, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
print(output)
