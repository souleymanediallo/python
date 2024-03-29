class Voiture:
    def __init__(self, marque, kilometrage):
        self.marque = marque
        self._kilometrage = kilometrage

    def get_kilometrage(self):
        return self._kilometrage

    def set_kilometrage(self, nouveau_kilometrage):
        if nouveau_kilometrage >= 0:
            self._kilometrage = nouveau_kilometrage
        else:
            print("Le kilométrage ne peut pas être négatif.")

    def affiche(self):
        print(f"Marque : {self.marque}, Kilométrage : {self._kilometrage}")


class Batterie:
    def __init__(self, capacite):
        self.capacite = capacite

    def affiche(self):
        print(f"Capacité de la batterie : {self.capacite} kWh")

class VoitureElectrique(Voiture):
    def __init__(self, marque, kilometrage, capacite):
        super().__init__(marque, kilometrage)
        self.batterie = Batterie(capacite)

    def affiche(self):
        super().affiche()
        self.batterie.affiche()


voiture = Voiture("Toyota", 100000)
voiture.affiche()

voiture.set_kilometrage(200000)
voiture.affiche()

voiture.set_kilometrage(-1000)
voiture.affiche()

voiture_electrique = VoitureElectrique("Tesla", 50000, 75)
voiture_electrique.affiche()