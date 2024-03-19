class Chien:
    def __init__(self, nom):
        self.nom = nom

    def parle(self):
        print("Ouaf !")


class Chat:
    def __init__(self, nom):
        self.nom = nom

    def parle(self):
        print("Miaou !")


def animal_parle(animal):
    animal.parle()

mon_chien = Chien("Rex")
mon_chat = Chat("Minou")

animal_parle(mon_chien)
animal_parle(mon_chat)