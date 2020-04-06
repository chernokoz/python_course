# here should be compose function


def compose(func1, func2, *args):
    def new_func(argument):
        tmp = argument
        for func_i in reversed(args):
            tmp = func_i(tmp)
        return func1(func2(tmp))
    return new_func
