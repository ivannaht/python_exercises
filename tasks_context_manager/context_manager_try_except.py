class Catcher:
    def __init__(self, *exceptions):
        self.exceptions = exceptions or Exception

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            return issubclass(exc_type, self.exceptions)
