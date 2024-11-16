import pytest

from tasks_oop.restaurant_2 import (ItalianRestaurant, SpanishRestaurant,
                                             AustrianRestaurant, OrderItem)


@pytest.mark.parametrize('menu, order, expected_result',
                         [(ItalianRestaurant, (OrderItem('first_course', 2, 21),
                                               OrderItem('second_course', 2, 35),
                                               OrderItem('dessert', 2, 18),
                                               OrderItem('beverage', 2, 4)),
                           'Pasta: 42, Potato with chicken: 70, Tiramisu: 36, Sparkling water: 8, '
                           'Total cost: 156'),
                          (SpanishRestaurant, (OrderItem('first_course', 2, 18),
                                               OrderItem('second_course', 2, 33),
                                               OrderItem('dessert', 2, 20.5),
                                               OrderItem('beverage', 2, 4.5)),
                           'Seafood soup: 36, Paella with seafood: 66, Banana mousse: 41.0, Juice: 9.0, '
                           'Total cost: 152.0'),
                          (AustrianRestaurant, (OrderItem('first_course', 2, 23.5),
                                                OrderItem('second_course', 2, 36),
                                                OrderItem('dessert', 2, 18.5),
                                                OrderItem('beverage', 2, 5.25)),
                           'Chicken soup: 47.0, Fried pike-perch fillet: 72, Milk cream strudel : 37.0, Lemonade: 10.5, '
                           'Total cost: 166.5')
                          ])
def test_calculate_total_cost(menu, order, expected_result):
    """
    verify calculate_total_cost function
    """

    selected_menu = menu()
    selected_menu.get_client_order(*order)
    assert selected_menu.calculate_total_cost() == expected_result
