from random import shuffle
from itertools import chain
from typing import Iterator, Any


class RandomLooper:
    """Реализуйте класс RandomLooper."""

    def __init__(self, *args) -> None:
        """При создании экземпляра класс должен принимать произвольное количество позиционных аргументов,
        каждый из которых является итерируемым объектом."""
        self.iterable = list(chain(*args))
        shuffle(self.iterable)
        self.iterable = iter(self.iterable)

    def __iter__(self) -> Iterator:
        """Экземпляр класса RandomLooper должен являться итератором, который генерирует в случайном порядке все элементы
        всех итерируемых объектов, переданных в конструктор, а затем возбуждает исключение StopIteration."""
        return self

    def __next__(self) -> Any:
        return next(self.iterable)
