
class Player:
    def __init__(self, health = 101, energy = 100):
        self.health = health
        self.energy = energy
        print(f"player created")

    def attack(self, monster, damage = 1 ):
        self.target = monster.health
        self.energy -= damage  # self.energy = self.emergy - damage
        print("attacking!")
class Monster:
    def __init__(self, health):
        self.health = health
        print("Monster Created")

player = Player()
monster = Monster(health=1000)
player.attack( monster,damage=80 )
print(monster.__dict__)

