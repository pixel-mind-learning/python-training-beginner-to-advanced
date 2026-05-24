from functools import reduce

nums = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14]

# def is_even(num):
#     return num % 2 == 0

# def map_nums(num):
    # return num * 2

# def sum_nums(a, b):
#     return a + b

even_nums = list(filter(lambda n: n % 2 == 0, nums))
map_nums = list(map(lambda n: n * 2, even_nums))
sum_nums = reduce(lambda a, b: a + b, map_nums)
print(sum_nums)
