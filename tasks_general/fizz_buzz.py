def fizz_buzz(number) -> str:
    """
    fizz_buzz function
    """

    if not isinstance(number, int):
        raise TypeError

    if number == 0:
        raise ValueError

    if number % 15 == 0:
        result = "FizzBuzz"
    elif number % 3 == 0:
        result = "Fizz"
    elif number % 5 == 0:
        result = "Buzz"
    else:
        result = str(number)

    return result
