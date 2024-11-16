from collections import OrderedDict
from collections import namedtuple

OrderItem = namedtuple("OrderItem", ["kind", "count", "price"])


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

    def get_client_order(self, *order: OrderItem):
        for item in order:
            self._add_item(item.kind, item.count, item.price)

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

    menu1.get_client_order(OrderItem('first_course', 2, 21),
                           OrderItem('second_course', 2, 35),
                           OrderItem('dessert', 2, 18),
                           OrderItem('beverage', 2, 4))

    menu2.get_client_order(OrderItem('first_course', 2, 18),
                           OrderItem('second_course', 2, 33),
                           OrderItem('dessert', 2, 20.5),
                           OrderItem('beverage', 2, 4.5))

    menu3.get_client_order(OrderItem('first_course', 2, 23.5),
                           OrderItem('second_course', 2, 36),
                           OrderItem('dessert', 2, 18.5),
                           OrderItem('beverage', 2, 5.25))

    print(menu1.calculate_total_cost())
    print(menu2.calculate_total_cost())
    print(menu3.calculate_total_cost())
