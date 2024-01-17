
class Player:
    #__init__ mrpkn salah satu duder method dari python spya otomatis dijalankan
    # setiap parameter yg ada wajib di set valuenya kalo ngga nanti error missing argument, jadi perlu set default valuenya
    def __init__(self, health = 101, energy = 100): # ini disebut onstructor
        self.health = health
        self.energy = energy
        # tambah f pada string untuk memunculkan nilai x
        print(f"player created")

    def attack(self):
        print("attacking!")
player = Player(201) # sama dengan -> player = Player(health=201)
#dunder method untuk mereturn object isi dari attr
print(player.__dict__)
# player.attack()
