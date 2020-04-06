import functools


def trace_if(funk):
    def trace_if_helper(function_to_decorate):
        @functools.wraps(function_to_decorate)
        def inner(*args, **kwargs):
            if funk(*args, **kwargs):
                print(function_to_decorate.__name__, args, kwargs)
            return function_to_decorate(*args, **kwargs)
        return inner
    return trace_if_helper
