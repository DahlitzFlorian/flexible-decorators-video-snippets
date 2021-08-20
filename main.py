import functools


def normal(func):
    return func


def shout(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()

    return wrapper


def whisper(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).lower()

    return wrapper


DECORATORS = {
    "normal": normal,
    "shout": shout,
    "whisper": whisper,
}

voice = input(f"Choose your voice ({', '.join(DECORATORS)}):")


@DECORATORS[voice]
def get_story():
    return "This is a sample text."


print(get_story())
