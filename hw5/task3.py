def contextmanager(gen):
    def helper(*args, **kwargs):
        class Inner:
            def __init__(self, gen, args, kwargs):
                self.gen = gen(*args, **kwargs)

            def __enter__(self):
                try:
                    return next(self.gen)
                except StopIteration:
                    raise RuntimeError("generator is empty()")

            def __exit__(self, exp_type, exp_value, exp_tr):
                try:
                    self.gen.throw(exp_type, exp_value, exp_tr)
                except StopIteration as exc:
                    return exc is not exp_value
        return Inner(gen, args, kwargs)
    return helper
