list_1 = [1, 2, 3, 4, 5, 5, 6, 7, 7, 8, 9, 0]


def square(num):
    return num ** 2


list_2 = list(map(square, list_1))
print(list_2)
list_3 = list(map(lambda num: num ** 2, list_1))
print(list_3)


def check_even(num):
    return num % 2 == 0


list_4 = list(filter(check_even, list_1))
print(list_4)
list_5 = list(filter(lambda num: num % 2 == 0, list_1))
print(list_5)

