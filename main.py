
class Player:
    #__init__ mrpkn salah satu duder method dari python spya otomatis dijalankan
    def __init__(self, health):
        self.x = health
        # tambah f pada string untuk memunculkan nilai x
        print(f"player created, x={self.x}")

    def attack(self):
        print("attacking!")
player = Player(100)
# player.attack()
