class MoneyBox:

    def __init__(self, capacity: int) -> None:
        self.check_coins_type(capacity)
        self.max_capacity = capacity
        self.coins = 0

    def can_add(self, v: int) -> bool:
        self.check_coins_type(v)
        return self.coins + v <= self.max_capacity

    def add(self, v: int) -> None:
        self.check_coins_type(v)
        if self.can_add(v):
            self.coins += v

    @staticmethod
    def check_coins_type(capacity: int) -> None:
        if type(capacity) is not int or capacity < 0:
            raise TypeError('Количество монет должно быть целым положительным числом')