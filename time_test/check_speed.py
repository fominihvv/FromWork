from string import ascii_uppercase, ascii_lowercase, digits
import math
import re
from zipfile import ZipFile
import csv
from datetime import datetime
import time
import calendar
from datetime import date, timedelta
import json
import random
from typing import Generator
from string import punctuation
from functools import reduce

# d = ['str'+str(i) for i in range(1000)]
my_month = ["янв", "фев", "мар", "апр", "май", "июн", "июл", "авг", "сен", "окт", "ноя", "дек"]
# test_month = list(set([random.choice(my_month) for _ in range(9)]))
# test_list = [random.choice(d) + ' 10 ' + random.choice(my_month) for _ in range(1000)]
extensions = "avi bat bin bmp cab cda csv dif dll doc docm docx dot dotx eml eps exe flv gif htm html ini iso jar jpg jpeg m4a mdb mid midi mov mp3 mp4 mpeg mpg msi mui pdf png pot potm potx ppam pps ppsm ppsx ppt pptm pptx psd pst pub rar rtf sldm sldx swf sys tif tiff tmp txt vob vsd vsdm vsdx vss vssm vst vstm vstx wav wbk wks wma wmd wmv xla xlam xll xlm xls xlsm xlsx xlt xltm xltx xps zip"


#    with open('words_400k.txt', 'r', encoding='utf-8') as file:
#        return  sorted({line:1 for line in file.read().upper().split() if line.endswith('ЕЯ')}, key = lambda x: (len(x), x))


# inp = ' '.join([str(random.choice(range(-100, 100))) for _ in range(10000)])
# lst_in = ['django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya','marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya','django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya','marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya','django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya','marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya','django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya','marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya','django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya','marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya','django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya','marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya','django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya','marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya','django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya','marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya','django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya','marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya','django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya','marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya','django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya','marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya','django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya','marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya','django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya','marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya']

stroka_chisel = ' '.join([str(random.randint(1, 5)) for _ in range(1000)])
stroka_bukv = ' '.join([random.choice('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm') for _ in range(100)])
stroka_slov = ' '.join(
    [ ''.join(random.choices('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890 ', k= random.randint(2, 10))) for _ in range(10)])
stroka_dubl = ' '.join([''.join(random.sample('qwerm', 3) + random.sample('qwerm', 3)) for _ in range(1000)])
stroka_dubl2 = ' '.join([''.join([random.choice(['bee', 'bee', ' geek ', 'sgfds', '.']) for _ in range(500)])])
stroka_bukv_i_chisel = [random.choice(['Q', 1]) for _ in range(1000)]
list_num = [random.randint(-100, 100) for _ in range(1_000_000)]
list_num_and_str = [random.choice([-3.5, 3.5, -2, -1, 2, 1, 0, 'r', 'R']) for _ in range(1_000)]
set_1 = set(random.randint(0, 1_000_000) for _ in range(1_000))
set_1.add(1000)
num_set = sorted(set_1)
spisok_failov = [''.join(random.choices('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890', k= random.randint(2, 10)))+'.'+random.choice(extensions.split()) for _ in range(1000)]


bool_none = [random.choice([True, False]) for _ in range(10_000)]

test_slovar = {k: i for k, i in enumerate(list_num)}
test_slovar2 = {k: i for k, i in enumerate(list_num)}


test_spisok = [i for i in list_num]
human = {
    "id": 1,
    "parents": [1, 2, 3, 4],
    "chief": {
        "name": "Paul",
        "age": 50
    },
    "age": 22
}

d = []


def nop(*rest, **kwargs):
    pass  # заглушка, функция ничего не делает



# numbers = list(range(1, 1_000_000))

class Alphabet:

    def __init__(self, lang: str):
        lng = {'en': list('abcdefghijklmnopqrstuvwxyz'), 'ru': list('абвгдежзийклмнопрстуфхцчшщъыьэюя')}
        self.alpha = lng[lang]

    def __iter__(self):
        return self

    def __next__(self):
        value = self.alpha.pop(0)
        self.alpha.append(value)
        return value


class Alphabet1:
    def __init__(self, language):
        if language == 'en':
            self.index = ord('a') - 1
            self.last_index = ord('z')
        elif language == 'ru':
            self.index = ord('а') - 1
            self.last_index = ord('я')
        self.first_index = self.index

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.last_index:
            self.index = self.first_index
        self.index += 1
        return chr(self.index)


class Matrix:
    def __init__(self, rows, cols, value=0):
        self.rows = rows
        self.cols = cols
        self.matrix = [[value] * cols for _ in range(rows)]

    def get_value(self, row, col):
        return self.matrix[row][col]

    def set_value(self, row, col, value):
        self.matrix[row][col] = value

    def copy(self, func=lambda x: x, transpose=False):
        if transpose:
            matrix = Matrix(self.cols, self.rows)
        else:
            matrix = Matrix(self.rows, self.cols)
        for row in range(self.rows):
            for col in range(self.cols):
                value = func(self.get_value(row, col))
                if transpose:
                    matrix.set_value(col, row, value)
                else:
                    matrix.set_value(row, col, value)
        return matrix

    def __str__(self):
        rows = (' '.join(map(str, row)) for row in self.matrix)
        return '\n'.join(rows)

    def __repr__(self):
        return f'Matrix({self.rows}, {self.cols})'

    def __pos__(self):
        return self.copy()

    def __neg__(self):
        return self.copy(func=lambda x: -x)

    def __invert__(self):
        return self.copy(transpose=True)

    def __round__(self, n=0):
        return self.copy(func=lambda x: round(x, n))

class Matrix2:

    def __init__(self, rows: int, cols: int, value: int = 0) -> None:
        self.rows = rows
        self.cols = cols
        self.value = value
        self.matrix = [[value] * self.cols for _ in range(self.rows)]

    def get_value(self, row: int, col: int) -> int:
        return self.matrix[row][col]

    def set_value(self, row: int, col: int, value: int) -> None:
        self.matrix[row][col] = value

    def __repr__(self) -> str:
        return f"Matrix({self.rows}, {self.cols})"

    def __str__(self) -> str:
        result = ''
        for row in self.matrix:
            result += ' '.join(list(map(str, row))) + '\n'
        return result.strip('\n')

    def __pos__(self) -> 'Matrix':
        result = Matrix(self.rows, self.cols)
        result.matrix = self.matrix[:]
        return result

    def __neg__(self) -> 'Matrix':
        result = Matrix(self.rows, self.cols)
        result.matrix = [[-x for x in row] for row in self.matrix]
        return result

    def __invert__(self) -> 'Matrix':
        result = Matrix(self.cols, self.rows)
        result.matrix = list(zip(*self.matrix))
        return result

    def __round__(self, n=0) -> 'Matrix':
        result = Matrix(self.rows, self.cols)
        result.matrix = [[round(x, n) for x in row] for row in self.matrix]
        return result



from itertools import accumulate
import operator
from math import factorial

ext = ('avi', 'mp4', 'mkv', 'mpg')

# моя функция
def check():
    #    with open('words_400k.txt', 'r', encoding='utf-8') as file:
    #        return {k:1 for k in file.read().split()}
    # return any(i < 3 for i in map(int, stroka_chisel.split()))
    # return min(enumerate(list_num), key=lambda x: x[1])[0], max(enumerate(list_num), key=lambda x: x[1])[0]
    # def is_prime(n: int) -> bool:
    #    if n == 2:
    #        return True
    #    elif not (n % 2) or n < 2:
    #        return False
    #    else:
    #        return all(bool(n % i) for i in range(3, round(n ** 0.5) + 1, 2))

    return str(test_slovar) == str(test_slovar2)




# чужая функция
def check2():

    return test_slovar.items() == test_slovar2.items()


# for i in range(100_000):
#    human['id'] = i
#    human['age'] = random.randint(0, 100)
#    human['chief']['age'] = random.randint(0, 100)
#    d.append(human)

print(len(test_slovar))
print(check())
print(check2())

test_range = 1

print('--------------Starting...------------------')

###############
# print2 = print
# print = nop
###############

time_1_monotonic = 0
for _ in range(test_range):
    start_monotonic = time.monotonic()
    check()
    time_1_monotonic += time.monotonic() - start_monotonic
print('25%... ', end='')
time_2_monotonic = 0
for _ in range(test_range):
    start_monotonic = time.monotonic()
    check2()
    time_2_monotonic += time.monotonic() - start_monotonic
print('50%... ', end='')
time_1_perf_counter = 0
for _ in range(test_range):
    start_perf_counter = time.perf_counter()
    check()
    time_1_perf_counter += time.perf_counter() - start_perf_counter
print('75%... ', end='')
time_2_perf_counter = 0
for _ in range(test_range):
    start_perf_counter = time.perf_counter()
    check2()
    time_2_perf_counter += time.perf_counter() - start_perf_counter
print('100%... ')


# print = print2

print('-------------- Тест через monotonic --------------')
print('---- Моя функция -- ', end='')
print(f'Время выполнения: {str(round(time_1_monotonic, 10))}')
print('-- Чужая функция -- ', end='')
print(f'Время выполнения: {str(round(time_2_monotonic, 10))}')
print('----------- Тест через perf.counter -------------')
print('---- Моя функция -- ', end='')
print(f'Время выполнения: {str(round(time_1_perf_counter, 10))}')
print('-- Чужая функция -- ', end='')
print(f'Время выполнения: {str(round(time_2_perf_counter, 10))}')
