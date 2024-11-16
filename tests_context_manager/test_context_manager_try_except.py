import pytest

from tasks_context_manager.context_manager_try_except import Catcher


@pytest.mark.parametrize('num1, num2, expected_result',
                         [(10, 2, 5), (0, 2, 0)])
def test_catcher_positive(num1, num2, expected_result):
    """
    verify catcher context manager positive scenarios
    """

    with Catcher():
        result = num1 / num2

        assert result == expected_result


@pytest.mark.parametrize('num1, num2',
                         [(1, 0), (1, '1')])
def test_catcher_negative1(num1, num2):
    """
    verify catcher context manager negative scenarios
    """

    with Catcher():
        result = num1 / num2

        assert result


@pytest.mark.parametrize('num1, num2, errors',
                         [(-1, 0, ZeroDivisionError),
                          (1, '1', TypeError),
                          (-1, 0, (TypeError, ZeroDivisionError))
                          ])
def test_catcher_negative2(num1, num2, errors):
    """
    verify catcher context manager negative scenarios
    """

    with Catcher(errors):
        result = num1 / num2

        assert result
