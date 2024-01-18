
class Player:
    def __init__(self, health = 101, energy = 100):
        self.health = health
        self.energy = energy

    def attack(self, monster, damage = 1 ):
        monster.health -= damage
        self.energy -= damage  # self.energy = self.emergy - damage
        print(f"attacking to monster, monster health {monster.health} left")
class Monster:
    def __init__(self, health):
        self.health = health

player1 = Player()
player2 = Player()

dragon = Monster(health=1000)
player1.attack( monster=dragon,damage=80 )
player2.attack( monster=dragon,damage=80 )

