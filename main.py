
class Player:
    def __init__(self, health = 101, energy = 100):
        self.health = health
        self.energy = energy

    def attack(self, target, damage = 1 ):
        target.health -= damage
        self.energy -= damage  # self.energy = self.emergy - damage
        print(f"monster health {target.health} left, your energy : {self.energy} left")
class Monster:
    def __init__(self, health = 200):
        self.health = health # dinamis
        self.health_init = self.health

    def attack(self):
        if self.health < self.health_init:
            print("siap serang balik")
        else :
            print("tidur")

player1 = Player()
player2 = Player()

dragon = Monster(health=500)
player1.attack( target=dragon,damage=20 )
player2.attack( target=dragon,damage=30 )

dragon.attack()

