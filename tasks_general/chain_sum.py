from operator import add
from functools import reduce


def chain_sum(*numbers) -> callable:
    """
    A function that receives numbers and returns itself.
    When the function is called without passing any numbers
    then the sum of all previously added numbers will be returned.
    """

    total = reduce(add, numbers) if numbers else 0

    def inner_chain_sum(*numbers) -> callable:
        nonlocal total

        if numbers:
            local_total = reduce(add, numbers)
            total += local_total

            return inner_chain_sum

        return total

    return inner_chain_sum


if __name__ == "__main__":
    assert chain_sum()() == 0
    assert chain_sum(50)(1)(200)() == 251
    assert chain_sum(5, 2)(2, 0.6, 0.4)() == 10.0
    assert chain_sum(5)(0.1)(-10)() == -4.9
