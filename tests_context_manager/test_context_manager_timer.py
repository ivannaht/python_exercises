import pytest

import time

from tasks_context_manager.context_manager_timer import Timer


@pytest.mark.parametrize('delay, test_time, expected_result',
                         [(1, 1, True),
                          (0, 0, True)
                          ])
def test_timer(delay, test_time, expected_result):
    """
    verify timer context manager
    """

    with Timer() as timer:
        time.sleep(delay)

    assert (timer.total >= test_time) is expected_result
