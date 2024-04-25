import datetime

# фиксируем и выводим время старта работы кода
print('print(*[i*2 for i in range(1,10,2)], file = fo)')
start = datetime.datetime.now()
print('Время старта: ' + str(start))

# код, время работы которого измеряем
with open('output1.log','w') as fo:
    for _ in range(10000):
        print(*[i*2 for i in range(1,10,2)], file = fo)

#фиксируем и выводим время окончания работы кода
finish = datetime.datetime.now()
print('Время окончания: ' + str(finish))

# вычитаем время старта из времени окончания
print('Время работы: ' + str(finish - start))
print()

print('[print(i*2, end = " ", file = fo) for i in range(1,10,2)]')
start = datetime.datetime.now()
print('Время старта: ' + str(start))

with open('output2.log','w') as fo:
    for _ in range(10000):
        [print(i*2, end = ' ', file = fo) for i in range(1,10,2)]

#фиксируем и выводим время окончания работы кода
finish = datetime.datetime.now()
print('Время окончания: ' + str(finish))

# вычитаем время старта из времени окончания
print('Время работы: ' + str(finish - start))
