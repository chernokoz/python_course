import functools


def n_times(times):
    def n_times_helper(function_to_decorate):
        @functools.wraps(function_to_decorate)
        def inner(*args, **kwargs):
            for _ in range(0, times):
                function_to_decorate(*args, **kwargs)

        return inner

    return n_times_helper
