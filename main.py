
class Player:
    def __init__(self, health = 101, energy = 100):
        self.health = health
        self.energy = energy
        print(f"player created")

    def attack(self, damage = 1):
        self.energy -= damage  # self.energy = self.emergy - damage
        print("attacking!")
class Monster:
    def __init__(self, health):
        self.health = health
        print("Monster Created")

player = Player()
monster = Monster(health=1000)
print(monster.__dict__)

