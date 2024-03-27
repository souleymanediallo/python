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


voiture = Voiture("Toyota", 100000)
voiture.affiche()

voiture.set_kilometrage(200000)
voiture.affiche()

voiture.set_kilometrage(-1000)
voiture.affiche()