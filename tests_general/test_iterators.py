import pytest

from tasks_general.iterators import (SimpleIterator, ReversedOperator,
                                             CycleIterator, PingPongIterator)


@pytest.mark.parametrize('test_class, test_iterable, expected_result',
                         [(SimpleIterator, (1, 5, 25), [1, 5, 25]),
                          (ReversedOperator, (1, 0, 5, 8, 25), [25, 8, 5, 0, 1])
                          ])
def test_iterators(test_class, test_iterable, expected_result):
    """
    verify iterators classes
    """

    iterator = test_class(test_iterable)
    assert list(iterator) == expected_result


@pytest.mark.parametrize('test_class, test_iterable, test_range, expected_result',
                         [(CycleIterator, (0, 1, 2), 3, [0, 1, 2]),
                          (CycleIterator, (0, 1, 2), 6, [0, 1, 2, 0, 1, 2]),
                          (PingPongIterator, (0, 1, 2), 3, [0, 1, 2]),
                          (PingPongIterator, (0, 1, 2), 14, [0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1]),
                          ])
def test_iterators_repeating(test_class, test_iterable, test_range, expected_result):
    """
    verify iterators classes with repeating
    """

    iterator = test_class(test_iterable)
    assert [next(iterator) for _ in range(test_range)] == expected_result
