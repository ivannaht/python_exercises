import pytest
from tasks_oop.warrior import Warrior, Knight, fight


@pytest.mark.parametrize('p1, p2, expected_result',
                         [((50, 5), (50, 7), [('round: 1', 'player1: health 50', 'player2: health 50'),
                                              ('round: 2', 'player1: health 50', 'player2: health 45'),
                                              ('round: 3', 'player1: health 43', 'player2: health 45'),
                                              ('round: 4', 'player1: health 43', 'player2: health 40'),
                                              ('round: 5', 'player1: health 36', 'player2: health 40'),
                                              ('round: 6', 'player1: health 36', 'player2: health 35'),
                                              ('round: 7', 'player1: health 29', 'player2: health 35'),
                                              ('round: 8', 'player1: health 29', 'player2: health 30'),
                                              ('round: 9', 'player1: health 22', 'player2: health 30'),
                                              ('round: 10', 'player1: health 22', 'player2: health 25'),
                                              ('round: 11', 'player1: health 15', 'player2: health 25'),
                                              ('round: 12', 'player1: health 15', 'player2: health 20'),
                                              ('round: 13', 'player1: health 8', 'player2: health 20'),
                                              ('round: 14', 'player1: health 8', 'player2: health 15'),
                                              ('round: 15', 'player1: health 1', 'player2: health 15'),
                                              ('round: 16', 'player1: health 1', 'player2: health 10'),
                                              ('round: 17', 'player1: health 0', 'player2: health 10')]),
                          ((60, 20), (60, 15), [('round: 1', 'player1: health 60', 'player2: health 60'),
                                                ('round: 2', 'player1: health 60', 'player2: health 40'),
                                                ('round: 3', 'player1: health 45', 'player2: health 40'),
                                                ('round: 4', 'player1: health 45', 'player2: health 20'),
                                                ('round: 5', 'player1: health 30', 'player2: health 20'),
                                                ('round: 6', 'player1: health 30', 'player2: health 0')])])
def test_fight(p1, p2, expected_result):
    """
    verify fight function
    """

    p1_health, p1_attack = p1
    p2_health, p2_attack = p2

    player1 = Warrior(p1_health, p1_attack)
    player2 = Knight(p2_health, p2_attack)

    assert fight(player1, player2) == expected_result
