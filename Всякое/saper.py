class Cell:
    def __init__(self, around_mines: int = 0, mine: bool = False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:
    def count_mines(self, x: int, y: int) -> int:
        res = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (0 <= x + i < self.n) and (0 <= y + j < self.n):
                    res += self.pole[x + i][y + j].mine
        return res

    def __init__(self, n: int, m: int):
        self.n = n
        self.mines_count = m
        self.pole = [[Cell() for _ in range(self.n)] for _ in range(self.n)]

    def init(self):
        from random import choice

        m = self.mines_count
        while m:
            x, y = choice(range(self.n)), choice(range(self.n))
            if not self.pole[x][y].mine:
                m -= 1
                self.pole[x][y].mine = True

        for x in range(self.n):
            for y in range(self.n):
                if not self.pole[x][y].mine:
                    self.pole[x][y].around_mines = self.count_mines(x, y)

    def show(self):
        for x in range(self.n):
            for y in range(self.n):
                if not self.pole[x][y].fl_open:
                    print('#', end=' ')
                else:
                    if self.pole[x][y].mine:
                        print('*', end=' ')
                    else:
                        print(self.pole[x][y].around_mines, end=' ')
            print()


pole_game = GamePole(5, 5)
pole_game.init()
while True:
    pole_game.show()
    x, y = map(int, input('Введите координаты клетки, или -1 -1 для выхода:').split())
    if x == -1 and y == -1:
        break
    pole_game.pole[x][y].fl_open = True
