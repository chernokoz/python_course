

def square(func):
    def inner(*args, **kwargs):
        return func(*args, **kwargs) ** 2
    return inner


def addsome(func):
    def inner(*args, **kwargs):
        return func(*args, **kwargs) + 42
    return inner


def succ(func):
    def inner(*args, **kwargs):
        return func(*args, **kwargs) + 1
    return inner


@succ
@addsome
@square
def identity(x):
    return x


if __name__ == "__main__":
    print(identity(2))
    print(identity(3))
