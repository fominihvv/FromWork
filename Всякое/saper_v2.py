from random import randint

"""Вы начинаете разрабатывать игру "Сапер". Для этого вам нужно уметь представлять и управлять игровым полем.
Будем полагать, что оно имеет размеры N x M клеток. Каждая клетка будет представлена объектом класса Cell и
содержать либо число мин вокруг этой клетки, либо саму мину."""


class Cell:
    """Следующий класс Cell описывает состояние одной ячейки игрового поля. Объекты этого класса создаются командой:
    cell = Cell()
    При этом в самом объекте создаются следующие локальные приватные свойства:
    __is_mine - булево значение True/False; True - в клетке находится мина, False - мина отсутствует;
    __number - число мин вокруг клетки (целое число от 0 до 8);
    __is_open - флаг того, открыта клетка или закрыта: True - открыта; False - закрыта."""

    def __init__(self):
        self.is_mine = False
        self.number = 0
        self.is_open = False

    """Для работы с этими приватными атрибутами объявите в классе Cell следующие объекты-свойства с именами:"""

    @property
    def is_mine(self) -> bool:
        """Для записи и чтения информации из атрибута __is_mine;"""
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, value: bool) -> None:
        """Для записи и чтения информации из атрибута __is_mine;"""
        if isinstance(value, bool):
            self.__is_mine = value
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def is_open(self) -> bool:
        """Для записи и чтения информации из атрибута __is_open."""
        return self.__is_open

    @is_open.setter
    def is_open(self, value: bool) -> None:
        """Для записи и чтения информации из атрибута __is_open."""
        if isinstance(value, bool):
            self.__is_open = value
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def number(self) -> int:
        """Для записи и чтения информации из атрибута __number;"""
        return self.__number

    @number.setter
    def number(self, value: int) -> None:
        """Для записи и чтения информации из атрибута __number;"""
        if type(value) is int and 0 <= value <= 8:
            self.__number = value
        else:
            raise ValueError("недопустимое значение атрибута")

    def __bool__(self) -> bool:
        """Которая возвращает True, если клетка закрыта и False - если открыта."""
        return not self.is_open


class GamePole:
    """Для начала в программе объявите класс GamePole, который будет создавать и управлять игровым полем.
    И, так как поле в игре одно, то нужно контролировать создание только одного объекта класса GamePole
    (используйте паттерн Singleton, о котором мы с вами говорили, когда рассматривали магический метод __new__())."""

    __exist = None

    def __new__(cls, *args, **kwargs):
        if cls.__exist is None:
            cls.__exist = object.__new__(cls)
            return cls.__exist
        else:
            return cls.__exist

    def __init__(self, n: int, m: int, total_mines: int) -> None:
        """Объект этого класса должен формироваться командой: pole = GamePole(N, M, total_mines)
        Объект pole должен иметь локальный приватный атрибут:
        __pole_cells - двумерный (вложенный) кортеж, размерами N x M элементов (N строк и M столбцов),
        состоящий из объектов класса Cell."""
        self.row = n
        self.col = m
        self.total_mines = total_mines
        self.show_flag = False

    """Для доступа к этой коллекции объявите в классе GamePole объект-свойство (property):"""

    @property
    def pole(self) -> list:
        """Только для чтения (получения) ссылки на коллекцию __pole_cells."""
        return self.__pole_cells

    def init_pole(self) -> None:
        """Для инициализации начального состояния игрового поля (расставляет мины и делает все клетки закрытыми);"""
        self.__pole_cells = [[Cell() for _ in range(self.col)] for _ in range(self.row)]
        count = self.total_mines
        while count:
            row, col = randint(0, self.row - 1), randint(0, self.col - 1)
            if not self.pole[row][col].is_mine:
                self.__pole_cells[row][col].is_mine = True
                count -= 1
        for i in range(self.row):
            for j in range(self.col):
                if not self.pole[i][j].is_mine:
                    self.__pole_cells[i][j].number = self.count_mines(i, j)

    def open_cell(self, i: int, j: int) -> None:
        """Открывает ячейку с индексами (i, j); нумерация индексов начинается с нуля;
        метод меняет значение атрибута __is_open объекта Cell в ячейке (i, j) на True;
        Необходимо проверять корректность индексов (i, j). Если индексы указаны некорректно,
        то генерируется исключение командой: raise IndexError('некорректные индексы i, j клетки игрового поля')"""
        if 0 <= i <= self.row and 0 <= j <= self.col:
            self.pole[i][j].__is_open = True
        else:
            raise IndexError('некорректные индексы i, j клетки игрового поля')

    def show_pole(self) -> None:
        """Отображает игровое поле в консоли"""
        for row in self.pole:
            for cell in row:
                if cell.is_open or self.show_flag:
                    print('*' if cell.is_mine else cell.number if cell.number else '.', end='')
                else:
                    print('#', end='')
            print()
        self.show_flag = False

    def count_mines(self, x: int, y: int) -> int:
        """Подсчитывает количество мин вокруг клетки"""
        res = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (0 <= x + i < self.row) and (0 <= y + j < self.col):
                    res += self.pole[x + i][y + j].is_mine
        return res

    """Расстановку мин выполняйте случайным образом по игровому полю (для этого удобно воспользоваться функцией 
    randint модуля random). После расстановки всех total_mines мин, вычислите их количество вокруг остальных клеток 
    (где нет мин). Область охвата - соседние (прилегающие) клетки (8 штук)."""


pole_game = GamePole(10, 10, 10)
flag_init = True
while True:
    if flag_init:
        count_mines = pole_game.total_mines
        pole_game.init_pole()
        flag_init = False
    pole_game.show_pole()
    ch = input(
        '1 - поставить мину, 2 - поставить флаг, 3 - показать поле 1 раз, 4 - перезапустить игру, 5 - выход. Ваш выбор? ')
    match ch:
        case '5':
            raise SystemExit(0)
        case '4':
            flag_init = True
        case '3':
            pole_game.show_flag = True
        case '2':
            x, y = map(int, input('Введите координаты клетки через пробел, или -1 -1 для выхода:').split())
            if x != -1 and y != -1:
                if pole_game.pole[x][y].is_open:
                    print('Эта клетка уже открыта')
                elif pole_game.pole[x][y].is_mine:
                    pole_game.show_flag = True
                    pole_game.show_pole()
                    print('Вы подорвались на мине. Конец игры.')
                    raise SystemExit(0)
                else:
                    pole_game.pole[x][y].is_open = True
        case '1':
            x, y = map(int, input('Введите координаты клетки через пробел, или -1 -1 для выхода:').split())
            if x != -1 and y != -1:
                if pole_game.pole[x][y].is_open:
                    print('Эта клетка уже открыта')
                elif pole_game.pole[x][y].is_mine:
                    print('Отлично!')
                    count_mines -= 1
                    pole_game.pole[x][y].is_open = True
                    if count_mines == 0:
                        pole_game.show_flag = True
                        pole_game.show_pole()
                        print('Вы победили!')
                        raise SystemExit(0)
                else:
                    print('Здесь нет мины...')
