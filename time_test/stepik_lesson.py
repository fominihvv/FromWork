from dataclasses import dataclass, field


@dataclass
class Promo:
    name: str
    discount: int
    items: list = field(default_factory=list)


@dataclass
class Product:
    name: str
    price: (int, float) = field(repr=False)

    def __hash__(self) -> int:
        return hash((self.name, self.price))


@dataclass
class Cart:
    goods: dict = field(default_factory=dict)
    discount: int = field(default=0)
    promo: Promo = field(default=None)
    total_without_promo: float = field(default=0)
    promo_or_discount: str = field(default='discount')

    @staticmethod
    def check_product(product: Product, amount: (int, float)) -> None:
        if not isinstance(product, Product):
            raise TypeError('Товар должен быть экземпляром класса Product')
        if type(amount) not in (int, float) or amount <= 0:
            raise ValueError('Количество должно быть положительным числом')

    def get_total(self) -> float:
        discount = 1 - self.discount / 100
        if self.promo_or_discount == 'discount' or (self.promo_or_discount == 'promo' and not self.promo.items):
            return self.total_without_promo * discount
        return sum(product.price * amount if product not in self.promo.items
                   else product.price * amount * discount for product, amount in self.goods.items())

    def add_product(self, product: Product, amount: (int, float) = 1) -> None:
        self.check_product(product, amount)
        self.goods[product] = self.goods.get(product, 0) + amount
        self.total_without_promo += product.price * amount

    def remove_product(self, product: Product, amount: (int, float) = 1) -> None:
        self.check_product(product, amount)
        if self.goods[product] <= amount:
            amount = self.goods[product]
            del self.goods[product]
        else:
            self.goods[product] -= amount
        self.total_without_promo -= product.price * amount

    def apply_discount(self, discount: int) -> None:
        if type(discount) is int and 1 <= discount <= 100:
            self.discount = discount
            self.promo_or_discount = 'discount'
        else:
            raise ValueError('Неправильное значение скидки')

    def apply_promo(self, promo: str) -> None:
        for item in ACTIVE_PROMO:
            if item.name == promo:
                self.discount = item.discount
                self.promo_or_discount = 'promo'
                self.promo = item
                print(f'Промокод {promo} успешно применился')
                return None
        print(f'Промокода {promo} не существует')


book = Product('Книга', 100.0)
usb = Product('Флешка', 50.0)
pen = Product('Ручка', 10.0)

ACTIVE_PROMO = [
    Promo('new', 20, [pen]),
    Promo('all_goods', 30),
    Promo('only_book', 40, [book]),
]

cart = Cart()
cart.add_product(book, 10)
cart.add_product(pen)
print('Тест 1. Считаем корзину...', end='   ')
print(cart.get_total(), end='   ')
assert cart.get_total() == 1010.0, 'Сумма корзины должна быть 1010.0'
print('OK')

cart = Cart()
cart.add_product(book, 10)
cart.add_product(pen)
print('Тест 2. Считаем корзину...', end='   ')
print(cart.get_total(), end='   ')
assert cart.get_total() == 1010.0, 'Сумма корзины должна быть 1010.0'
print('OK')

print('Тест 3. Применяем промокод "only_book"...', end='   ')
cart.apply_promo('only_book')
print(cart.get_total(), end='   ')
assert cart.get_total() == 610.0, 'После применения промокода на книгу сумма корзины должна быть 610.0'
print('OK')

print('Тест 4. Применяем скидку 10%...', end='   ')
cart.apply_discount(10)
print(cart.get_total(), end='   ')
assert cart.get_total() == 909.0, 'После применения скидки 10% сумма корзины должна быть 909.0'
print('OK')

print('Тест 5. Применяем промокод "only_book"...', end='   ')
cart.apply_promo('only_book')
print(cart.get_total(), end='   ')
assert cart.get_total() == 610.0, 'После применения промокода на книгу сумма корзины должна быть 610.0'
print('OK')

print('Тест 6. Применяем скидку 10%...', end='   ')
cart.apply_discount(10)
print(cart.get_total(), end='   ')
assert cart.get_total() == 909.0, 'После применения скидки 10% сумма корзины должна быть 909.0'
print('OK')

print('Тест 7. Применяем промокод "new"...', end='   ')
cart.apply_promo('new')
print(cart.get_total(), end='   ')
assert cart.get_total() == 1008.0, 'После применения промокода на ручку сумма корзины должна быть 1008.0'
print('OK')

print('Тест 8. Применяем промокод "only_book"...', end='   ')
cart.apply_promo('only_book')
print(cart.get_total(), end='   ')
assert cart.get_total() == 610.0, 'После применения промокода на книгу сумма корзины должна быть 610.0'
print('OK')

print('Тест 9. Применяем скидку 10%...', end='   ')
cart.apply_discount(10)
print(cart.get_total(), end='   ')
assert cart.get_total() == 909.0, 'После применения скидки 10% сумма корзины должна быть 909.0'
print('OK')

print('Все тесты пройдены')

