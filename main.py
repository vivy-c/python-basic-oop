
class Player:
    def __init__(self, health = 101, energy = 100):
        self.health = health
        self.energy = energy

    def attack(self, target, damage = 1 ):
        target.health -= damage
        self.energy -= damage  # self.energy = self.emergy - damage
        # ditaruh sini supaya di print di bagian atas
        print(f"player attacking {damage} damage to monster")
        if target.is_attacked():
            self.health -= target.damage
    def show_info(self):
        print(f"player health : {self.health}")
        print(f"player energy : {self.energy}")
class Monster:
    def __init__(self, health = 200):
        self.health = health # dinamis
        self.health_init = self.health
        self.damage = 10
    # made monster attack to boolean method
    def is_attacked(self):
        print(f"monster attacking {self.damage} damage to player")
        return self.health < self.health_init

    def show_info(self):
        print(f"monster health {self.health} left")

player1 = Player()
player2 = Player()

dragon = Monster(health=500)
player1.attack( target=dragon,damage=20 )
# player2.attack( target=dragon,damage=30 )

player1.show_info()
dragon.show_info()

