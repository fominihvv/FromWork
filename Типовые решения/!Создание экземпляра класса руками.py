class CellInteger:
    def __new__(cls, *args, **kwargs) -> 'CellInteger':
        instance = object.__new__(cls)
        instance.__init__(*args, **kwargs)
        return instance

    def __init__(self, start_value: int = 0) -> None:
        self.value = start_value


class TableValues:

    def __init__(self, rows, cols, cell: type) -> None:
        if cell is None:
            raise ValueError('параметр cell не указан')
        self.rows = rows
        self.cols = cols
        self.cells = [[cell.__new__(cell) for _ in range(self.cols)] for _ in range(self.rows)]