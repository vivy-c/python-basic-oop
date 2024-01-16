#OBJECT
#access modifier
# __ --> private access
# _ --> protected access
class Player:
    #inner class
    #attribute
    name = "joni" # public access
    __salary = 10_000_000_000
    #method
    def get_salary(self):
        return self.__salary

#outter class
#outter class bisa akses attr name karena name itu public
# print(Player)
player = Player()
print(f"nama {player.name} berhasil dibuat")

player.name = "vivy cahyani"
print(f"{player.name} dalah nama baru")
player.salary = 30_000_000_000 # salary = attr baru & != attr __salary
print(player.salary)
print(player.get_salary())
