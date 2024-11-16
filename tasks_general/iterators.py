class Iterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0

    def __iter__(self):
        return self


class SimpleIterator(Iterator):
    def __next__(self):
        if self.index >= len(self.iterable):
            raise StopIteration

        element = self.iterable[self.index]
        self.index += 1

        return element


class ReversedOperator(Iterator):
    def __init__(self, iterable):
        super().__init__(iterable)
        self.index = len(self.iterable) - 1

    def __next__(self):
        if self.index < 0:
            raise StopIteration

        element = self.iterable[self.index]
        self.index -= 1

        return element


class CycleIterator(Iterator):
    def __next__(self):
        if self.index >= len(self.iterable):
            self.index = 0

        element = self.iterable[self.index]
        self.index += 1

        return element


class PingPongIterator(Iterator):
    def __init__(self, iterable):
        super().__init__(iterable)
        self.move_back = False

    def __next__(self):
        element = self.iterable[self.index]
        if self.index == len(self.iterable) - 1:
            self.move_back = True
        elif self.index == 0:
            self.move_back = False

        self.index = self.index + 1 if not self.move_back else self.index - 1

        return element
