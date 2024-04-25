class Point:

    def __init__(self, x=0, y=0):
        self.__x = 0
        self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)

    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Координаты должны быть int или float')

    def get_coord(self):
        return self.__x, self.__y


pt = Point()
print(pt.get_coord())
pt.__x = 1
print(pt.get_coord())
pt.set_coord(10, 20)
print(pt.get_coord())
