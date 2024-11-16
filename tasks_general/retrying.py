import random


def retry(func):
    """
    Decorator which will retry inner function if it failed
    """

    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(e)
                continue

    return wrapper


@retry
def positive_function(a, b):
    result = random.randint(a, b)

    if result <= 0:
        raise ValueError(result, "Failed because result is not positive")
    return result


def retry_param(tries=None):
    """
    Decorator which will retry inner function several times if it failes
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            times = 0

            while True:
                if tries and (tries - times) == 0:
                    break
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(e)
                    times += 1
                    continue

        return wrapper

    return decorator


@retry_param()
def negative_function(a, b):
    result = random.randint(a, b)

    if result >= 0:
        raise ValueError(result, "Failed because result is not negative")

    return result


@retry_param(tries=5)
def zero_function(a, b):
    result = random.randint(a, b)

    if result != 0:
        raise ValueError(result, "Failed because result is not zero")

    return result


if __name__ == "__main__":
    print(positive_function(a=-10, b=10))
    print(negative_function(a=-10, b=10))
    print(zero_function(a=-10, b=10))
