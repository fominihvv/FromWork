from functools import reduce

data= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def product_of_odds(data):   # data - список целых чисел
    result = reduce(lambda x, y: x * y, filter(lambda x: x % 2 == 1, data), 1)
    return result

def arithmetic_operation(operation):
    return {'+': lambda x, y: x+y, '-': lambda x, y: x-y, '*': lambda x, y: x*y, '/': lambda x, y: x/y}[operation]

print(product_of_odds(data))