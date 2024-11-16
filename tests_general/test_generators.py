import pytest

from tasks_general.generators import (simple_generator, reversed_generator,
                                              cycle_generator, ping_pong_generator)


@pytest.mark.parametrize('test_generator,test_iterable, expected_result',
                         [(simple_generator, (1, 5, 25), [1, 5, 25]),
                          (reversed_generator, (1, 0, 5, 8, 25), [25, 8, 5, 0, 1])
                          ])
def test_generators(test_generator, test_iterable, expected_result):
    """
    verify generators
    """

    generator = test_generator(test_iterable)
    assert list(generator) == expected_result


@pytest.mark.parametrize('test_generator,test_iterable, r, expected_result',
                         [(cycle_generator, (0, 1, 2), 3, [0, 1, 2]),
                          (cycle_generator, (0, 1, 2), 6, [0, 1, 2, 0, 1, 2]),
                          (ping_pong_generator, (0, 1, 2), 3, [0, 1, 2]),
                          (ping_pong_generator, (0, 1, 2), 5, [0, 1, 2, 1, 0]),
                          ])
def test_generators_repeating(test_generator, test_iterable, r, expected_result):
    """
    verify generators with repeating
    """

    generator = test_generator(test_iterable)
    assert [next(generator) for _ in range(r)] == expected_result
