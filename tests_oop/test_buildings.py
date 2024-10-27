import pytest
from tasks_oop.buildings import Building


@pytest.mark.parametrize('arguments, expected_result',
                         [((1, 2.5, 4.2, 1.25, 101), ('Building(1, 2.5, 4.2, 1.25, 101)\n'
                                                      "Coordinates of corners: {'north-east': [2.25, 6.7], 'south-east': [1, 6.7], "
                                                      "'south-west': [1, 2.5], 'north-west': [2.25, 2.5]}\n"
                                                      'Area: 5.25\n'
                                                      'Volume: 530.25')),
                          ((0, 0, 10.5, 2.546), ('Building(0, 0, 10.5, 2.546, 10)\n'
                                                 "Coordinates of corners: {'north-east': [2.546, 10.5], 'south-east': [0, 10.5], 'south-west': [0, 0], 'north-west': [2.546, 0]}\n"
                                                 'Area: 26.732999999999997\n'
                                                 'Volume: 267.33'))
                          ])
def test_show_building(arguments, expected_result):
    """
    verify show_building function
    """
    south, west, width_WE, width_NS, *height = arguments
    b = Building(south, west, width_WE, width_NS, *height)

    assert b.show_building() == expected_result
