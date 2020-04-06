import time


class Timer:
    def __init__(self):
        self.start = 0
        self.delta = 0
        self.end = 0

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, *args):
        self.end = time.time()
        self.delta = self.end - self.start
        print(self.delta)
