dictionnaire = {"nom": "John", "age": 30, "ville": "Paris"}
print(dictionnaire)


# Étape 2: Ajouter des paires clé-valeur
dictionnaire["emploi"] = "Développeur"
dictionnaire["hobbies"] = ["Vélo", "Lecture"]
print(dictionnaire)

# Étape 3: Modifier des valeurs
dictionnaire["age"] = 31
print(dictionnaire)

# Étape 4: Accéder à des valeurs
print(dictionnaire["nom"])

# Étape 5: Supprimer des paires clé-valeur
del dictionnaire["hobbies"]
print(dictionnaire)

# Étape 6: Parcourir un dictionnaire
for cle in dictionnaire:
    print(cle)
    print(dictionnaire[cle])


# Étape 7: Parcourir un dictionnaire
for cle, valeur in dictionnaire.items():
    print(f"{cle} : {valeur}")
