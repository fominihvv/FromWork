class MoneyBox:
    def __init__(self, capacity: int) -> None:
        if type(capacity) is not int:
            raise TypeError('Количество монет должно быть целым числом')
        self.max_capacity = capacity
        self.coins = 0


    def can_add(self, v: int) -> bool:
        if type(v) is not int:
            raise TypeError('Количество монет должно быть целым числом')
        if self.max_capacity < v and self.coins + v > self.max_capacity:
            return False
        return True

    def add(self, v: int) -> None:
        if self.can_add(v):
            self.coins += v