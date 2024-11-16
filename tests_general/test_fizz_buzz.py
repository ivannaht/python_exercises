import pytest

from tasks_general.fizz_buzz import fizz_buzz


@pytest.mark.parametrize('number, expected_result',
                         [(1, '1'),
                          (3, 'Fizz'),
                          (5, 'Buzz'),
                          (-15, 'FizzBuzz'),
                          (45, 'FizzBuzz')])
def test_fizz_buzz_positive(number, expected_result):
    """
    verify positive scenarios for fizz_buss function
    """

    assert fizz_buzz(number) == expected_result


@pytest.mark.parametrize('number, error',
                         [(0, ValueError),
                          (1.5, TypeError),
                          ("abc", TypeError),
                          (False, ValueError),
                          ([1, 2, 3], TypeError),
                          ({1, 2, 3}, TypeError)
                          ])
def test_fizz_buzz_negative(number, error):
    """
    verify negative scenarios for fizz_buss function
    """

    with pytest.raises(error):
        fizz_buzz(number)
