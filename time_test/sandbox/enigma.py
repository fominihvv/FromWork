import time
from string import ascii_uppercase
MAX_LETTERS = 26


class Rotor:
    ROTORS = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
              1: 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
              2: 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
              3: 'BDFHJLCPRTXVZNYEIWGAKMUSQO',
              4: 'ESOVPZJAYQUIRHXLNFTGKDCMWB',
              5: 'VZBRGITYUPSDNHLXAWMJQOFECK',
              6: 'JPGVOUMFYQBENHZRDKASXLICTW',
              7: 'NZJHGRCXMYSWBOUFAIVLPEKQDT',
              8: 'FKQHTLXOCBJSPDZRAMEWNIUYGV',
              'beta': 'LEYJVCNIXWPBQMDRTAKZGFUHOS',
              'gamma': 'FSOKANUERHMBTIYCWLQPZXVGJD'
              }

    def __init__(self, rotor_number: (int, str), shift: int = 0) -> None:
        self.rotor_number = rotor_number
        self.rotor_forward = {k: v for v, k in zip(self.ROTORS[self.rotor_number], ascii_uppercase)}
        self.rotor_backward = {k: v for v, k in zip(ascii_uppercase, self.ROTORS[self.rotor_number])}
        self.ABC_IND = {k: v for v, k in enumerate(ascii_uppercase)}
        self.IND_ABC = dict(enumerate(ascii_uppercase))
        self.shift = shift
        self.flag_shift = False

    def __call__(self, letter: str, direction: bool = False) -> str:
        rotors = self.rotor_backward if direction else self.rotor_forward
        result = self.IND_ABC[(self.ABC_IND[letter] + self.shift) % MAX_LETTERS]
        result = rotors[result]
        result = self.IND_ABC[(self.ABC_IND[result] - self.shift) % MAX_LETTERS]
        return result


class Reflector:
    REFLECTORS = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                  1: 'YRUHQSLDPXNGOKMIEBFZCWVJAT',
                  2: 'FVPJIAOYEDRZXWGCTKUQSBNMHL',
                  3: 'ENKQAUYWJICOPBLMDXZVFTHRGS',
                  4: 'RDOBJNTKVEHMLFCWZAXGYIPSUQ',
                  }

    def __init__(self, reflector: int) -> None:
        self.reflector = dict(zip(self.REFLECTORS[0], self.REFLECTORS[reflector]))

    def __call__(self, letter: str) -> str:
        return self.reflector[letter]


class Enigma:

    def __init__(self) -> None:
        self.reflector = [Reflector(i) for i in range(5)]
        self.rotors = []

    @staticmethod
    def normalize_text(text: str):
        return (letter for letter in text.upper() if letter in ascii_uppercase)

    def rotorize(self, letter: str, direction: bool = False) -> str:
        rotors = self.rotors[::-1] if direction else self.rotors
        for rotor in rotors:
            letter = rotor(letter, direction=direction)
        return letter

    def check_shift(self) -> None:
        rotors_step = {1: (17,), 2: (5,), 3: (22,), 4: (10,), 5: (0,), 6: (0, 13), 7: (0, 13), 8: (0, 13)}
        rotor1, rotor2, rotor3 = self.rotors

        rotor1.shift = (rotor1.shift + 1) % MAX_LETTERS
        if rotor1.shift in rotors_step[rotor1.rotor_number]:
            rotor2.shift = (rotor2.shift + 1) % MAX_LETTERS

        if rotor2.flag_shift:
            rotor2.shift = (rotor2.shift + 1) % MAX_LETTERS
            rotor3.shift = (rotor3.shift + 1) % MAX_LETTERS
            rotor2.flag_shift = False

        rotor2.flag_shift = rotor2.shift + 1 in rotors_step[rotor2.rotor_number]

    def __call__(self, text: str, reflector: int, rotor1: int, shift1: int, rotor2: int, shift2: int, rotor3: int,
                 shift3: int) -> str:
        self.rotors = [Rotor(rotor3, shift3), Rotor(rotor2, shift2), Rotor(rotor1, shift1)]
        result = ''
        for letter in self.normalize_text(text):
            self.check_shift()
            letter = self.rotorize(letter, False)
            letter = self.reflector[reflector](letter)
            letter = self.rotorize(letter, True)
            result += letter
        return result


enigma = Enigma()

start = time.perf_counter()
assert enigma('AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA', 1, 2, 3, 2, 3, 2, 3) == 'BGDMBTZUONCIZMORCPNVLGOVLMURTNZNDROPETXLPLYCMIBICXITUCM'
print(time.perf_counter() - start)
