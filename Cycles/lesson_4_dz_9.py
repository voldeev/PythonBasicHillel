import random

random_list = random.sample(range(1, 101), random.randint(3, 10))
print("Випадковий список:", random_list)

final_list = [random_list[0], random_list[2], random_list[-2]]
print("Фінальний список:", final_list)
