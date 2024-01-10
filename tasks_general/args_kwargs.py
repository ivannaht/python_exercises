def calc_sum(*args):
    return sum(args)


print(calc_sum(5, 10, 15))


def double_numbers(*args):
    list_doubles = []
    for arg in args:
        list_doubles.append(arg * 2)
    return list_doubles


print(double_numbers(5, 10, 15))


def select_color(**kwargs):
    if 'color' in kwargs:
        return f"You selected {kwargs['color']} color"
    else:
        return "No color was found"


print(select_color(color='green', taste='sweet'))


def convert_currency(*args, **kwargs):
    if kwargs['currency'] == 'USD' and kwargs['action'] == 'purchase':
        k = 38.4
        return round((sum(args) / k), 2)
    elif kwargs['currency'] == 'USD' and kwargs['action'] == 'sale':
        k = 39
        return round((sum(args) / k), 2)
    elif kwargs['currency'] == 'EUR' and kwargs['action'] == 'purchase':
        k = 42
        return round((sum(args) / k), 2)
    elif kwargs['currency'] == 'EUR' and kwargs['action'] == 'sale':
        k = 43
        return round((sum(args) / k), 2)
    else:
        return 'It is impossible to convert'


print(convert_currency(4300, 700, currency='USD', action='sale'))
print(convert_currency(4300, 700, currency='USD', action='purchase'))
print(convert_currency(4000, 300, currency='EUR', action='sale'))
print(convert_currency(4000, 200, currency='EUR', action='purchase'))
print(convert_currency(4300, 700, currency='UAH', action='purchase'))
