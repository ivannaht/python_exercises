import random
import time


def func_performance_timer(func):
    """
    Decorator that logs the time of function execution
    """

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(func.__name__, time.time() - start)

        return result

    return wrapper


@func_performance_timer
def sort_list_rand():
    """
    Function that returns sorted random list with delay
    """

    rand_list = [random.randint(-100, 100) for i in range(10)]
    time.sleep(1)
    rand_list.sort()

    return rand_list


@func_performance_timer
def sorted_built_in_rand():
    """
    Function that returns sorted random list with delay
    """

    rand_list = [random.randint(-100, 100) for i in range(10)]
    time.sleep(1)

    return sorted(rand_list)


if __name__ == "__main__":
    for func in [sort_list_rand, sorted_built_in_rand]:
        print(func())
