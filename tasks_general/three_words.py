def three_words(text) -> bool:
    """
    three_words function
    checks if the string contains three words in succession
    """

    if not isinstance(text, str):
        raise TypeError

    if text == '':
        raise ValueError

    elements = text.split()

    result = []

    for element in elements:
        if element.isalpha():
            result.append(element)
        else:
            result = []

        if len(result) >= 3:
            return True
        continue

    return False


def three_words_2(text) -> bool:
    """
    solution 2
    three_words function
    checks if the string contains three words in succession
    """

    elements = text.split()

    for i in range(len(elements) - 2):

        result = [word for word in elements[i: i + 3] if word.isalpha()]

        if len(result) == 3:
            return True

    return False
