import logging

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
        print(f"Liste {self.nom}:")
        for element in self:
            print(f"- {element}")

list = MaListe("Courses")
list.ajouter("Pain")
list.ajouter("Beurre")
list.ajouter("Lait")
list.afficher()

list.enlever("Beurre")
list.afficher()






