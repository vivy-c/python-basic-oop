
class Player:
    def __init__(self, health = 101, energy = 100):
        self.health = health
        self.energy = energy
        print(f"player created")

    def attack(self, monster, damage = 1 ):
        monster.health -= damage
        self.energy -= damage  # self.energy = self.emergy - damage
        print(f"attacking to monster, monster health {monster.health} left")
class Monster:
    def __init__(self, health):
        self.health = health
        print("Monster Created")

player = Player()
monster = Monster(health=1000)
player.attack( monster,damage=80 )
print(monster.__dict__)

