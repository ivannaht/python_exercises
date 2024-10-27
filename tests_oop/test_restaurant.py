import pytest

from tasks_oop.restaurant import ItalianRestaurant, SpanishRestaurant, \
    AustrianRestaurant

menu1 = ItalianRestaurant()
menu2 = SpanishRestaurant()
menu3 = AustrianRestaurant()


@pytest.mark.parametrize('menu, order, expected_result',
                         [(menu1, ((2, 10), (2, 20), (2, 15), (4, 3)),
                           ('Pasta: 20, Potato with chicken: 40, Tiramisu: 30, '
                            'Sparkling water: 12, Total cost: 102')),
                          (menu2, ((2, 8), (2, 25), (2, 10), (4, 5)),
                           ('Seafood soup: 16, Paella with seafood: 50, Banana mousse: 20, '
                            'Juice: 20, Total cost: 106')),
                          (menu3, ((2, 9.2), (2, 30.5), (2, 12.3), (4, 4.4)),
                           ('Chicken soup: 18.4, Fried pike-perch fillet: 61.0, Milk cream strudel : 24.6, '
                            'Lemonade: 17.6, Total cost: 121.6'))
                          ])
def test_calculate_total_cost(menu, order, expected_result):
    """
    verify calculate_total_cost function
    """

    menu.get_client_order(*order)
    assert menu.calculate_total_cost() == expected_result
