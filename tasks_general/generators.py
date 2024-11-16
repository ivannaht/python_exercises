def simple_generator(iterable):
    index = 0
    while index < len(iterable):
        yield iterable[index]
        index += 1


def reversed_generator(iterable):
    index = len(iterable) - 1
    while index >= 0:
        yield iterable[index]
        index -= 1


def cycle_generator(iterable):
    index = 0
    while True:
        if index >= len(iterable):
            index = 0

        yield iterable[index]
        index += 1


def ping_pong_generator(iterable):
    index = 0
    asc = True

    while True:
        element = iterable[index]
        if asc and index == len(iterable) - 1:
            asc = False
        elif asc is False and index == 0:
            asc = True

        index = index + 1 if asc else index - 1
        yield element
