class Player:
    def __init__(self, health, attack):
        self.health = health
        self.attack = attack

    @property
    def is_alive(self):
        return self.health > 0

    def hit(self, player: 'Player'):
        player.lose_health(self.attack)

    def lose_health(self, damage: int):
        self.health = max(0, self.health - damage)


class Warrior(Player):
    def __init__(self, health, attack):
        super().__init__(health, attack)


class Knight(Player):
    def __init__(self, health, attack):
        super().__init__(health, attack)


def fight(player1: Warrior, player2: Knight):
    round = 1
    game = [(f'round: {round}', f'player1: health {player1.health}', f'player2: health {player2.health}')]

    while player1.is_alive:
        player1.hit(player2)
        round += 1
        game.append((f'round: {round}', f'player1: health {player1.health}', f'player2: health {player2.health}'))

        if not player2.is_alive:
            break

        player2.hit(player1)
        round += 1
        game.append((f'round: {round}', f'player1: health {player1.health}', f'player2: health {player2.health}'))

    return game


if __name__ == '__main__':
    player1 = Warrior(50, 5)
    player2 = Knight(50, 7)

    print(fight(player1, player2))
