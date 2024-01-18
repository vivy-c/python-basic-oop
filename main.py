
class Player:
    def __init__(self, health = 101, energy = 100):
        self.health = health
        self.energy = energy

    def attack(self, target, damage = 1 ):
        target.health -= damage
        self.energy -= damage  # self.energy = self.emergy - damage
        print(f"attacking to monster, target health {target.health} left")
class Monster:
    def __init__(self, health):
        self.health = health

player1 = Player()
player2 = Player()

dragon = Monster(health=1000)
player1.attack( target=dragon,damage=80 )
player2.attack( target=dragon,damage=80 )

