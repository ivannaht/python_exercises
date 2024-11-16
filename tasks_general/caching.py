from datetime import date


def cache(func):
    """
    Decorator which remembers answers for given arguments.
    When argument is repeated then decorator does not make a call to a function
    and uses the previously returned result
    """

    cached_results = {}

    def wrapper(arg):
        if arg not in cached_results:
            print("function is called with '{}'".format(arg))
            cached_results[arg] = func(arg)
        return cached_results[arg]

    return wrapper


@cache
def calculate_age(dob):
    days_in_year = 365.2425
    age = int((date.today() - dob).days / days_in_year)

    return age


if __name__ == "__main__":
    print(calculate_age(date(2000, 10, 21)))
    print(calculate_age(date(2000, 10, 21)))
