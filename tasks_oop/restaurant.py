from collections import OrderedDict
from functools import partialmethod


class Restaurant:
    menu = {'first_course': 'First Course',
            'second_course': 'Second Course',
            'dessert': 'Dessert',
            'beverage': 'Beverage'}

    def __init__(self):
        self.order = OrderedDict()

    def _add_item(self, key, count, price):
        if key not in self.menu:
            raise ValueError(f'{key} is not available in the menu')

        name = self.menu[key]

        if name not in self.order:
            self.order[name] = 0
        self.order[name] += count * price

    _add_first_course = partialmethod(_add_item, "first_course")
    _add_second_course = partialmethod(_add_item, "second_course")
    _add_dessert = partialmethod(_add_item, "dessert")
    _add_beverage = partialmethod(_add_item, "beverage")

    def get_client_order(self, first, second, desert, beverages):
        self._add_first_course(first[0], first[1])
        self._add_second_course(second[0], second[1])
        self._add_dessert(desert[0], desert[1])
        self._add_beverage(beverages[0], beverages[1])

    def calculate_total_cost(self):
        total_cost = 0
        result = []
        for item, price in self.order.items():
            total_cost += price
            result.append(f"{item}: {price}")
        result.append(f"Total cost: {total_cost}")

        return ", ".join(result)


class ItalianRestaurant(Restaurant):
    menu = {'first_course': 'Pasta',
            'second_course': 'Potato with chicken',
            'dessert': 'Tiramisu',
            'beverage': 'Sparkling water'}


class SpanishRestaurant(Restaurant):
    menu = {'first_course': 'Seafood soup',
            'second_course': 'Paella with seafood',
            'dessert': 'Banana mousse',
            'beverage': 'Juice'}


class AustrianRestaurant(Restaurant):
    menu = {'first_course': 'Chicken soup',
            'second_course': 'Fried pike-perch fillet',
            'dessert': 'Milk cream strudel ',
            'beverage': 'Lemonade'}


if __name__ == '__main__':
    menu1 = ItalianRestaurant()
    menu2 = SpanishRestaurant()
    menu3 = AustrianRestaurant()

    menu1.get_client_order((2, 10), (2, 20), (2, 15), (4, 3))
    menu2.get_client_order((2, 8), (2, 25), (2, 10), (4, 5))
    menu3.get_client_order((2, 9.2), (2, 30.5), (2, 12.3), (4, 4.4))

    print(menu1.calculate_total_cost())
    print(menu2.calculate_total_cost())
    print(menu3.calculate_total_cost())
