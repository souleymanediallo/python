class Document:
    def __init__(self, titre):
        self.titre = titre

    def afficher_titre(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Livre(Document):
    def afficher_titre(self):
        print(f"Titre du livre: {self.titre}")


class Journal(Document):
    def afficher_titre(self):
        print(f"Titre du journal: {self.titre}")

documents = [Livre("1984"), Journal("The New York Times")]

for document in documents:
    document.afficher_titre()
