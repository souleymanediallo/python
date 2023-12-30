import logging
import os
import json


from constants import DATA_DIR

LOGGER = logging.getLogger()

class MaListe(list):
    def __init__(self, nom):
        self.nom = nom

    def __str__(self):
        return self.nom

    def ajouter(self, element):
        if not isinstance(element, str):
            LOGGER.error("L'élément doit être une chaîne de caractères")

        if element in self:
            LOGGER.warning("L'élément existe déjà dans la liste")
            return False

        self.append(element)
        return True

    def enlever(self, element):
        if element in self:
            self.remove(element)
            return True
        return False

    def afficher(self):
        print(f"Ma Liste de {self.nom} :")
        for element in self:
            print(f"- {element}")

    def sauvegarder(self):
        fichier = os.path.join(DATA_DIR, f"{self.nom}.json")
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)

        with open(fichier, "w") as f:
            json.dump(self, f, indent=4)
        return True


if __name__ == '__main__':
    ma_liste = MaListe("Courses")
    ma_liste.ajouter("Pain")
    ma_liste.ajouter("Beurre")
    ma_liste.ajouter("Lait")
    ma_liste.sauvegarder()

    ma_liste.enlever("Beurre")
    ma_liste.afficher()

    # ma_liste.ajouter(1)
    # ma_liste.ajouter("Pain")








