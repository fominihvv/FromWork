class ObjList:
    """Объекты этого класса создаются командой:
    obj = ObjList(data), где data - строка с некоторой информацией.
    Также в каждом объекте obj класса ObjList должны создаваться следующие локальные атрибуты:
    __data - ссылка на строку с данными;
    __prev - ссылка на предыдущий объект связного списка (если объекта нет, то __prev = None);
    __next - ссылка на следующий объект связного списка (если объекта нет, то __next = None)."""

    def __init__(self, data: str) -> None:
        self.data = data
        self.prev = None
        self.next = None

    @property
    def data(self) -> str:
        return self.__data

    @data.setter
    def data(self, value: str) -> None:
        self.__data = value

    @property
    def prev(self) -> 'ObjList' or None:
        return self.__prev or None

    @prev.setter
    def prev(self, value: 'ObjList') -> None:
        if isinstance(value, ObjList) or value is None:
            self.__prev = value
        else:
            raise TypeError('Допускаются только объекты класса ObjList или None')

    @property
    def next(self) -> 'ObjList' or None:
        return self.__next or None

    @next.setter
    def next(self, value: 'ObjList') -> None:
        if isinstance(value, ObjList) or value is None:
            self.__next = value
        else:
            raise TypeError('Допускаются только объекты класса ObjList или None')


class LinkedList:
    """Класс LinkedList. Список из связанных между собой объектов класса ObjList.
    Объекты класса LinkedList должны создаваться командой:
    linked_lst = LinkedList()"""

    def __init__(self) -> None:
        """Аттрибуты: head - ссылка на первый объект связного списка (если список пуст, то head = None);
        tail - ссылка на последний объект связного списка (если список пуст, то tail = None)."""
        self.head = None
        self.tail = None
        self.__size = 0

    def __find_object(self, idx: int) -> 'ObjList' or None:
        """Возвращает элемент по индексу, индекс отсчитывается с нуля"""
        if type(idx) is int:
            if 0 <= idx < self.__size:
                pointer = self.head
                idx -= 1
                while 0 <= idx:
                    pointer = pointer.next
                    idx -= 1
                return pointer
            else:
                raise IndexError("Выход за границы списка")
        else:
            raise TypeError("Допускаются только целые числа")

    def add_obj(self, obj: ObjList) -> None:
        """Добавляет новый объект obj класса ObjList в конец связного списка;"""
        if isinstance(obj, ObjList):
            self.__size += 1
            if self.head is None:  #Если пустой список
                self.head = obj
                self.tail = obj
            else:
                if self.head.next is None:  #Если один элемент
                    self.head.next = obj
                    obj.prev = self.head
                else:
                    self.tail.next = obj
                    obj.prev = self.tail
                self.tail = obj
        else:
            raise TypeError('Допускаются только объекты класса ObjList')

    def remove_obj(self, idx: int) -> None:
        """Удаляет объект класса ObjList из связного списка по его (индексу); индекс отсчитывается с нуля."""
        pointer = self.__find_object(idx)
        if pointer is not None:
            if pointer == self.head:  #Если первый элемент
                if self.head.next is None:  #Если один элемент в списке
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif pointer == self.tail:  #Если последний элемент
                self.tail = self.tail.prev
            else:
                pointer.prev.next = pointer.next
                pointer.next.prev = pointer.prev
        self.__size -= 1

    def __len__(self) -> int:
        """len(linked_lst) - возвращает число объектов в связном списке;"""
        return self.__size

    def linked_list(self, idx: int) -> str or None:
        """Возвращает строку __data, хранящуюся в объекте под индексом idx, индекс отсчитывается с нуля"""
        pointer = self.__find_object(idx)
        if pointer is not None:
            return pointer.data

    def __call__(self, *args, **kwargs) -> str:
        return self.linked_list(args[0])
