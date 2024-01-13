def nth_smallest(lst, n):
    """function that returns the nth smallest integer
    (the smallest integer is the first smallest, the second smallest integer is the second smallest, etc)"""
    k = len(lst)
    if n < 1 or n > k:
        raise IndexError("n should be less than 1 and greater than length of list")
    else:
        for i in range(n):
            if lst[i] > k:
                result = lst[i]
        return result


print(nth_smallest([5, 1, 8, 9], 2))
print(nth_smallest([1, 3, 5, 7], 3))
print(nth_smallest([1, 3, 5, 7], 4))

try:
    print(nth_smallest([1, 3, 5, 7], 5))
except IndexError as e:
    print(e)


def find_odd(lst):
    """function that takes a list and finds the list of integers that appear an odd number of times."""
    new_lst = []
    for num in lst:
        if lst.count(num) % 2 != 0 and num not in new_lst:
            new_lst.append(num)
    return new_lst


print(find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))
print(find_odd([20, 1, 1, 2, 1, 2, 3, 3, 5, 5, 4, 20, 4, 5]))
print(find_odd([10]))


def probability(lst, n):
    """function that returns the probability of choosing a number greater than or equal to n from the list"""
    k = 0
    for num in lst:
        if num >= n:
            k += 1

    return round(k * 100 / len(lst), 1)


print(probability([5, 1, 8, 9], 6))
print(probability([7, 4, 17, 14, 12, 3], 16))
print(probability([4, 6, 2, 9, 15, 18, 8, 2, 10, 8], 6))


def filter_list(lst):
    """function that takes a list of non-negative integers
    and strings and return a new list without the strings"""
    return [el for el in lst if type(el) == int]


print(filter_list([1, 2, "gdfsdf", 5]))
print(filter_list(["aasf", "1", "123", 123, 0, 15]))


def add_indexes(lst):
    """function which returns the list but with each element's index in the list added to itself"""
    new_lst = []
    for i, num in enumerate(lst):
        new_lst.append(num + i)
    return new_lst


print(add_indexes([1, 2, 3]))
print(add_indexes([5, 4, 3, 2, 1]))
print(add_indexes([0, -1, -2, -3, -4]))
