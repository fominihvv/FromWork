#assert CentralBank
"""cb = CentralBank
assert cb is not None, "Объекты класса CentralBank создаваться не должны, должно просто возвращаться значение None "

r = MoneyR(45_000)
assert r.volume == 45_000, "Неверно присваивается значение"
assert r.cb is None, "Кошелёк при создании должен быть не зарегистрирован"
CentralBank.register(r)
assert r.cb is not None, "Кошелёк должен быть уже зарегистрирован"

r1 = MoneyR(45_000.0005)
CentralBank.register(r1)
assert r == r1, "Сравнение кошельков вернуло False, при значениях 45_000 и 45_000.0005"

d = MoneyD(45_000 / cb.rates['rub'])
e = MoneyE(45_000 / cb.rates['rub'] * cb.rates['euro'])

try:
    d == r
except ValueError as err:
    assert err != "Неизвестен курс валют.", "Не генерируется исключение для незарегистрированного кошелька"

CentralBank.register(d)
CentralBank.register(e)

assert r == d, "Неверно реализованно сравнение кошельков"
assert e == d, "Неверно реализованно сравнение кошельков"
assert r == e, "Неверно реализованно сравнение кошельков"

e2 = e = MoneyE(40_000 / cb.rates['rub'] * cb.rates['euro'])
CentralBank.register(e2)
assert e2 < r, "Неверно реализованно сравнение кошельков"""

"""try:
    tr = Triangle(-5, 4, 3)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError
    
try:
    a[100] = 25.5
except IndexError as err:
    assert str(err) == 'неверный индекс для доступа к элементам массива', "не сгенерировалось исключение IndexError при записи"
"""