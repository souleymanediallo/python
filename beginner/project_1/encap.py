class CompteBancaire:
    def __init__(self, proprietaire, solde=0):
        self.proprietaire = proprietaire
        self._solde = solde

    @property
    def solde(self):
        return self._solde

    def deposer(self, montant):
        if montant > 0:
            self._solde += montant
            print("Dépôt effectué.")

    def retirer(self, montant):
        if 0 < montant <= self._solde:
            self._solde -= montant
            print("Retrait effectué.")
        else:
            print("Fonds insuffisants.")

compte = CompteBancaire("Alice", 1000)
compte.deposer(500)
compte.retirer(200)
print(compte.solde)