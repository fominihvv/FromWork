n1, n2, n3, n4 = [int(i) for i in input().split('.')]
# 0.0.0.0
if n1 == 0 and n2 == 0 and n3 == 0 and n4 == 0:
    print(True)
    exit(0)
elif n1 > 255 or n2 > 255 or n3 > 255 or n4 > 255:
    print(False)
    exit(0)
elif (0 < n1 < 128) or (0 < n2 < 128 and (n1 != 0 and n2 == 0)) or (
        0 < n3 < 128 and (n1 != 0 and n2 != 0 and n3 == 0)) or 0 < n4 < 128:
    print(False)
    exit(0)
# 0.x.x.x
elif n1 == 0:
    print(False)
    exit(0)
# x.0.0.x x.0.x.0 x.0.x.x x.x.0.x
elif (n2 == 0 and n3 == 0 and n4 != 0) or (n2 == 0 and n3 != 0 and n4 != 0) or (n2 == 0 and n3 != 0 and n4 == 0) or (
        n2 != 0 and n3 == 0 and n4 != 0):
    print(False)
    exit(0)
else:
    # Проверяем первый октет
    last, curr = 0, 0
    while n1:
        curr = n1 % 2
        if not curr and last:
            print(False)
            exit(0)
        n1 //= 2
        last = curr
    # Проверяем второй октет
    last, curr = 0, 0
    while n2:
        curr = n2 % 2
        if not curr and last:
            print(False)
            exit(0)
        n2 //= 2
        last = curr
    # Проверяем третий октет
    last, curr = 0, 0
    while n3:
        curr = n3 % 2
        if not curr and last:
            print(False)
            exit(0)
        n3 //= 2
        last = curr
    # Проверяем четвёртый октет
    last, curr = 0, 0
    while n4:
        curr = n4 % 2
        if not curr and last:
            print(False)
            exit(0)
        n4 //= 2
        last = curr
    print(True)
