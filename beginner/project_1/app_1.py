class Division:
    @staticmethod
    def diviser(x, y):
        try:
            resultat = x / y
        except ZeroDivisionError:
            print("Erreur: Division par zéro.")
        else:
            print(f"Le résultat est {resultat}")

Division.diviser(10, 2)
Division.diviser(5, 0)