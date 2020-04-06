def implicit_int(cls):

    def inner(_, __):
        return 0
    cls.__getattr__ = inner
    return cls
