my_list = [10, 2, 20, 3, 30, 40]
result = filter(lambda x: (x % 10 == 0), my_list)
print("Numbers divisible by 10 are", list(result))
