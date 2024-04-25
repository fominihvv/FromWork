from re import fullmatch
from string import ascii_uppercase, ascii_lowercase, digits


class Registration:

    def __init__(self, login: str, password: str) -> None:
        """один аргумент — логин пользователя. Метод __init__ должен сохранить переданный логин через сеттер"""
        self.login = login
        self.password = password

    @property
    def login(self) -> str:
        """возвращает значение self.__login;"""
        return self.__login

    @login.setter
    def login(self, login: str) -> None:
        """Свойство сеттер login, принимает значение нового логина. Новое значение мы должны проверить на следующее:
        строковое значение: если поступают другие типы данных, необходимо вызвать исключение raise TypeError. Логин, так
        как является почтой, должен содержать один символ собаки «@». В случае, если в логине отсутствует символ «@»,
        вызываем исключение при помощи строки raise ValueError. Логин должен содержать символ «.» после символа «@».
        В случае, если после @ нет точки, вызываем исключение при помощи строки raise ValueError
        Если значение проходит проверку, новое значение логина сохраняется в атрибут self.__login"""
        if not isinstance(login, str):
            raise TypeError()
        if fullmatch(r'^\w+@\w+\.\w+$', login) is None:
            raise ValueError()
        self.__login = login

    @staticmethod
    def is_include_digit(password: str) -> bool:
        return not set(digits).isdisjoint(password)

    @staticmethod
    def is_include_register(password: str) -> bool:
        return not set(ascii_lowercase).isdisjoint(password) and not set(ascii_uppercase).isdisjoint(password)

    @staticmethod
    def is_include_only_latin(password: str) -> bool:
        return set(password).issubset(ascii_lowercase + ascii_uppercase + digits)

    @staticmethod
    def check_password_dictionary(password: str) -> bool:
        with open('easy_passwords.txt', 'r') as f:
            for line in f:
                if password == line.strip('\n'):
                    return True
            return False

    @property
    def password(self) -> str:
        """возвращает значение self.__password"""
        return self.__password

    @password.setter
    def password(self, password: str) -> None:
        """Принимает значение нового пароля. Его необходимо перед сохранением проверить на следующее:
        1. Новое значение пароля должно быть строкой (не список, словарь и т.д. ), в противном случае
           вызываем исключение TypeError("Пароль должен быть строкой")
        2. Длина нового пароля должна быть от 5 до 11 символов, в противном случае вызывать исключение
           ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        3. Новый пароль должен содержать хотя бы одну цифру. Для этого создаем staticmethod is_include_digit,
           который проходит по всем элементам строки и проверяет наличие цифр. В случае отсутствия цифрового символа
           вызываем исключение: ValueError('Пароль должен содержать хотя бы одну цифру')
        4. Строка password должна содержать элементы верхнего и нижнего регистра. Создаем staticmethod
           is_include_all_register, который с помощью цикла проверяет элементы строчки на регистр. В случае ошибки
           вызываем: ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
        5. Строка password помимо цифр должна содержать только латинские символы. Для этого создайте staticmethod
           is_include_only_latin , который проверяет каждый элемент нового значения на принадлежность к латинскому
           алфавиту (проверка должна быть как в верхнем, так и нижнем регистре). В случае, если встретится нелатинский
           символ, вызвать ошибку ValueError('Пароль должен содержать только латинский алфавит'). Подсказка: из модуля
           string можно импортировать переменную ascii_letters, она хранит в себе все латинские символы в верхнем и
           нижнем регистре
        6. Пароль не должен совпадать ни с одним из легких паролей, хранящихся в файле easy_passwords.txt.
           Сохраните данный файл к себе в папку с вашей программой и не меняйте название. С помощью staticmethod
           создаем метод check_password_dictionary и проверяем наличие нашего пароля в данном файле. Если значение
           совпадет со значением из файла, то в сеттер вызываем исключение: (
           ValueError('Ваш пароль содержится в списке самых легких'))"""
        if not isinstance(password, str):
            raise TypeError('Пароль должен быть строкой')
        if 12 <= len(password) or len(password) <= 4:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        if not self.is_include_digit(password):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        if not self.is_include_register(password):
            raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
        if not self.is_include_only_latin(password):
            raise ValueError('Пароль должен содержать только латинский алфавит')
        if self.check_password_dictionary(password):
            raise ValueError('Ваш пароль содержится в списке самых легких')
        self.__password = password


try:
    s2 = Registration("fga", "asd12")
except ValueError as e:
    pass
else:
    raise ValueError("Registration('fga', 'asd12') как можно записать такой логин?")

try:
    s2 = Registration("fg@a", "asd12")
except ValueError as e:
    pass
else:
    raise ValueError("Registration('fg@a', 'asd12') как можно записать такой логин?")

s2 = Registration("translate@gmail.com", "as1SNdf")
try:
    s2.login = "asdsa12asd."
except ValueError as e:
    pass
else:
    raise ValueError("asdsa12asd как можно записать такой логин?")

try:
    s2.login = "asdsa12@asd"
except ValueError as e:
    pass
else:
    raise ValueError("asdsa12@asd как можно записать такой логин?")
assert Registration.check_password_dictionary('QwerTy123'), 'проверка на пароль в слове не работает'

try:
    s2.password = "QwerTy123"
except ValueError as e:
    pass
else:
    raise ValueError("QwerTy123 хранится в словаре паролей, как его можно было сохранить?")

try:
    s2.password = "KissasSAd1f"
except ValueError as e:
    pass
else:
    raise ValueError("KissasSAd1f хранится в словаре паролей, как его можно было сохранить?")

try:
    s2.password = "124244242"
except ValueError as e:
    pass
else:
    raise ValueError("124244242 пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "RYIWUhjkdbfjfgdsffds"
except ValueError as e:
    pass
else:
    raise ValueError("RYIWUhjkdbfjfgdsffds пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "CaT"
except ValueError as e:
    pass
else:
    raise ValueError("CaT пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "monkey"
except ValueError as e:
    pass
else:
    raise ValueError("monkey пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "QwerTy123"
except ValueError as e:
    pass
else:
    raise ValueError("QwerTy123 пароль есть в слове, нельзя его использовать")

try:
    s2.password = "HelloQEWq"
except ValueError as e:
    pass
else:
    raise ValueError("HelloQEWq пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = [4, 32]
except TypeError as e:
    pass
else:
    raise TypeError("Пароль должен быть строкой")

try:
    s2.password = 123456
except TypeError as e:
    pass
else:
    raise TypeError("Пароль должен быть строкой")

print('U r hacked Pentagon')
