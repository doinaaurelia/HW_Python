# 32. Дана последовательность чисел. 
# Получить список уникальных элементов заданной последовательности.

from random import randint

def create_list(size, m, n):
    return [randint(m, n) for i in range(size)]

def get_unic_value(list):
    return [i for i in set(list)]

size = 10
m = 1
n = 10

origin = create_list(size, m, n)
print(origin)
print(get_unic_value(origin))


## вторая задача

def parse(line):
    num = ''
    for i in line:
        if not num and i in '-':
            num += i
            continue
        if i in '1234567890.':
            num += i
        elif num:
            yield float(num)
            num = ''
        if i in OPERATORS or i in '()':
            yield i
    if num:
        yield float(num)