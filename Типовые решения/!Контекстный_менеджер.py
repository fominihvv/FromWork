from contextlib import contextmanager
from sys import stdout


@contextmanager
def reversed_print():
    stdout_write_original = stdout.write
    stdout.write = lambda x: stdout_write_original(x[::-1])
    yield
    stdout.write = stdout_write_original


class UpperPrint:
    """Реализуйте класс UpperPrint. При создании экземпляра класс не должен принимать никаких аргументов."""

    def upper_print(self, text):
        self.orig_stdout_write(text.upper())

    def __enter__(self, *args, **kwargs):
        self.orig_stdout_write = stdout.write
        stdout.write = self.upper_print

    def __exit__(self, exc_type, exc_val, exc_tb):
        stdout.write = self.orig_stdout_write
        return True