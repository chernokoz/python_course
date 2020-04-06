class ViewCls:
    def __init__(self, inst):
        self.__obj = inst
        self.__deleted = set()

    def __getattr__(self, item):
        if item in self.__deleted:
            raise AttributeError(item)
        return getattr(self.__obj, item)

    def __delattr__(self, item):
        if item in self.__deleted:
            raise AttributeError(item)
        if item in self.__dict__:
            super().__delattr__(item)
        elif not hasattr(self.__obj, item):
            raise AttributeError(f"{item} is not existing attr")
        self.__deleted.add(item)


class View(type):
    def __new__(mcs, name, bases, attrs, **kwargs):
        attrs["view"] = lambda x: ViewCls(x)
        return super().__new__(mcs, name, bases, attrs)
