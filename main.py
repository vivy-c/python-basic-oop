
class Player:
    def __init__(self, health = 101, energy = 100):
        self.health = health
        self.energy = energy
        print(f"player created")

    def attack(self, damage = 1):
        self.energy -= damage  # self.energy = self.emergy - damage
        print("attacking!")
player = Player()
player.attack()
player.attack(damage=34)

print(player.__dict__)
