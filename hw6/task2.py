from functools import wraps


def final(func):
    @wraps(func)
    def inner(*args, **kwargs):
        return func(args, kwargs)
    inner.is_final = True
    return inner


class WithFinals(type):
    def __new__(mcs, name, bases, attrs, **kwargs):
        to_return = super().__new__(mcs, name, bases, attrs)
        methods = set()
        parents = to_return.mro()
        for parent in parents:
            for i in parent.__dict__.keys():
                if not callable(parent.__dict__[i]):
                    continue
                elif i not in methods:
                    methods.add(i)
                elif callable(parent.__dict__[i]) and i in methods\
                        and hasattr(parent.__dict__[i], "is_final") and \
                        parent.__dict__[i].is_final:
                    raise TypeError("Error! It was final"
                                    " method in one of the parents!")
                else:
                    methods.add(i)
        return to_return
