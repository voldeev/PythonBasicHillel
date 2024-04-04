def common_elements():
    multiples_of_3 = [num for num in range(3, 100, 3)]
    multiples_of_5 = [num for num in range(5, 100, 5)]
    common_set = set(multiples_of_3) & set(multiples_of_5)
    return common_set

print(common_elements())
