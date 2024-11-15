import random
import time
from random import randint, choice
from string import ascii_lowercase, digits, ascii_letters

# -----------------------------------------

orders_count = 200_000
start = randint(1, 50_000)
end = randint(1, 100_000) + start
inp = [f'{start} {end} {choice([1, 2, 3, 4])}' for _ in range(orders_count)]
request_count = 200_000
start = randint(1, 100_000)
end = randint(1, 100_000) + start
inp_2 = [f'{start} {end} {choice([1, 2])}' for _ in range(request_count)]

# -----------------------------------------


extensions = "avi bat bin bmp cab cda csv dif dll doc docm docx dot dotx eml eps exe flv gif htm html ini iso jar jpg jpeg m4a mdb mid midi mov mp3 mp4 mpeg mpg msi mui pdf png pot potm potx ppam pps ppsm ppsx ppt pptm pptx psd pst pub rar rtf sldm sldx swf sys tif tiff tmp txt vob vsd vsdm vsdx vss vssm vst vstm vstx wav wbk wks wma wmd wmv xla xlam xll xlm xls xlsm xlsx xlt xltm xltx xps zip"

stroka_chisel = ' '.join([str(random.randint(-5, 5)) for _ in range(1000)])
print("Строка чисел - Готово")

stroka_bukv = ''.join([random.choice('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm') for _ in range(1_000)])
print("Строка букв - Готово")

stroka_bukv_lower = ''.join([random.choice(ascii_lowercase) for _ in range(1_000_000)])
print("Строка букв в мал. регистре - Готово")

stroka_bukv_i_chisel = [random.choice(['Q', 1]) for _ in range(1000)]
print("Строка букв и чисел - Готово")

stroka_slov = ' '.join(
    [''.join(random.choices('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890 ', k=random.randint(2, 10)))
     for _ in range(1_000)])
print("Строка слов - Готово")

spisok_slov = [
    ''.join(random.choices('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890', k=random.randint(2, 10)))
    for _ in range(1_000)]
print("Список слов - Готово")

list_num = [random.randint(-1_000, 1_000) for _ in range(1_00)]
print("Список чисел - Готово")

str_num_sort = ' '.join(map(str, sorted(list_num)))
print("Строка чисел отсортированная - Готово")

list_num_and_ch = [random.choice([-3.5, 3.5, -2, -1, 2, 1, 0, 'r', 'R']) for _ in range(1_000)]
print("Список чисел и символов - Готово")

list_list = [[random.randint(-100, 100) for _ in range(random.randint(1, 10))] for _ in range(50_000)]
print("Список списков - Готово")

list_tuple = [tuple(random.randint(-100, 100) for _ in range(random.randint(1, 10))) for _ in range(10_000)]
print("Список кортежей - Готово")

set_1 = set(random.randint(0, 1_000) for _ in range(1_000))
print("Множество - Готово")

spisok_failov = [''.join(random.choices('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890',
                                        k=random.randint(2, 10))) + '.' + random.choice(extensions.split()) for _ in
                 range(1000)]
print("Список файлов - Готово")

bool_none = [random.choice([True, False]) for _ in range(1_000)]
print("Список True-False - Готово")

test_slovar = {k: i for k, i in enumerate(list_num, 1)}
test_slovar2 = {k: i for k, i in enumerate(list_num, 1)}
print("Словари - Готово")

# print(inp)
# print(inp_2)


cache = {}
pattern = ascii_letters + digits + '-?!$#@_'
password = '12345asdf@#'


def check():
    size: int = 1_000
    up_fill: int = 0
    down_fill: int = 0
    fill = lambda i, j: i + 1 if i == j else up_fill if j > i else down_fill
    return [[fill(i, j) for j in range(size)] for i in range(size)]

def check2():
    size: int = 5_000
    up_fill: int = 0
    down_fill: int = 0
    return [[down_fill] * rows + [rows + 1] + [up_fill] * (size - rows - 1) for rows in range(size)]

# Для проверки что, это работает как надо
#print(check())
#print(check2())

# Сколько раз тестить


test_range = 1
print('--------------Starting...------------------')

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

print('-------------- Тест через monotonic -------------')
print('----- check --- ', end='')
print(f'Время выполнения: {str(round(time_1_monotonic, 10))}')
print('----- check2 -- ', end='')
print(f'Время выполнения: {str(round(time_2_monotonic, 10))}')

print('----------- Тест через perf.counter -------------')
print('----- check --- ', end='')
print(f'Время выполнения: {str(round(time_1_perf_counter, 10))}')
print('----- check2 -- ', end='')
print(f'Время выполнения: {str(round(time_2_perf_counter, 10))}')
