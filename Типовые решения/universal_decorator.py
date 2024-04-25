from functools import wraps


def retry(*args_deco, **kwargs_deco):
    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
                return func(*args, **kwargs)

        return wrapper

    return decorator

