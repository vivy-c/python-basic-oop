
class Player:
    def __init__(self, name, health = 101, energy = 100):
        self.name = name
        self.health = health
        self.energy = energy

    def attack(self, target, damage = 1 ):
        target.health -= damage
        self.energy -= damage  # self.energy = self.emergy - damage
        # ditaruh sini supaya di print di bagian atas
        print(f"{self.name} attacking {damage} damage to {target.name}")
        if target.is_attacked(player_name=self.name):
            self.health -= target.damage
    def show_info(self):
        print(f"{self.name} health : {self.health}")
        print(f"{self.name} energy : {self.energy}")
class Monster:
    def __init__(self, name,  health = 200):
        self.name = name
        self.health = health # dinamis
        self.health_init = self.health
        self.damage = 10
    # made monster attack to boolean method
    def is_attacked(self, player_name):
        print(f"{self.name} attacking {self.damage} damage to {player_name}")
        return self.health < self.health_init

    def show_info(self):
        print(f"{self.name} health {self.health} left")

player1 = Player(name="naruto")
player2 = Player(name="sasuke")

monster1 = Monster(health=500, name="jubii")
monster2 = Monster(health=400, name="garaga")
player1.attack( target=monster1,damage=20 )
player2.attack( target=monster2,damage=30 )

player1.show_info()
monster2.show_info()

