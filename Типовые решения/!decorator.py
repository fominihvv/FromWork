from types import FunctionType
from functools import wraps


def introduce(value: int) -> any:
    def actual_decorator(func: FunctionType) -> any:
        @wraps(func)
        def wrapper(*args, **kwargs) -> any:
            print(func.__name__, value)
            return func(*args, **kwargs)

        return wrapper

    return actual_decorator


@introduce(2)
def identity(x):
    return x


print(identity(20))
