import time


class Timer:
    def __init__(self):
        self.total = 0
        self.start = None

    def __enter__(self):
        self.total = 0
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.total += (time.time() - self.start)


if __name__ == "__main__":
    with Timer() as timer:
        time.sleep(0)

    print(timer.total)
