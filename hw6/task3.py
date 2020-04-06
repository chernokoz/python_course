class SingletonIterator:
    def __init__(self, cls):
        iter_list = list()
        for i in cls._cache:
            iter_list.append(i[1])
        self.iterator = iter(iter_list)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterator)


class Singleton(type):
    def __iter__(cls):
        return SingletonIterator(cls)

    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cls._cache = list()

    def __call__(cls, *args):
        for i in cls._cache:
            if i[0] == args:
                return i[1]
        obj = super().__call__(*args)
        cls._cache.append((args, obj))
        return obj
