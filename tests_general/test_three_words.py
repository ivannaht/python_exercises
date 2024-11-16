import pytest

from tasks_general.three_words import three_words, three_words_2


@pytest.mark.parametrize('text, expected_result',
                         [('Hi', False),
                          ('1 2 3 4 5', False),
                          ('This text is without any number', True),
                          ('27 is greater than 26', True),
                          ('Today is 27.09.2024. Yesterday was 26th of September.', False)
                          ])
def test_three_words_positive(text, expected_result):
    """
    verify positive scenarios for three_words function
    """

    assert three_words(text) == expected_result


@pytest.mark.parametrize('text, error',
                         [(123, TypeError),
                          (100.0, TypeError),
                          (['abc'], TypeError),
                          ({'This text is without any number'}, TypeError),
                          ({'Number': 5}, TypeError),
                          ('', ValueError)
                          ])
def test_three_words_negative(text, error):
    """
    verify negative scenarios for three_words function
    """

    with pytest.raises(error):
        three_words(text)


@pytest.mark.parametrize('text, expected_result',
                         [('Hi', False),
                          ('1 2 3 4 5', False),
                          ('This text is without any number', True),
                          ('27 is greater than 26', True),
                          ('Today is 27.09.2024. Yesterday was 26th of September.', False)
                          ])
def test_three_words_2_positive(text, expected_result):
    """
    verify positive scenarios for three_words_2 function
    """

    assert three_words_2(text) == expected_result
