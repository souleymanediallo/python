str = "Bonjour tout le monde !" # On définit une variable str qui contient une chaîne de caractères
print(str) # On affiche la variable str
print(type(str)) # On affiche le type de la variable str
print(str[0]) # On affiche le premier caractère de la chaîne de caractères
print(str[-1]) # On affiche le dernier caractère de la chaîne de caractères
print(str[0:7]) # On affiche les 7 premiers caractères de la chaîne de caractères
print(str[8:]) # On affiche les caractères de la chaîne de caractères à partir du 8ème caractère
print(str[0:7:2]) # On affiche les caractères de la chaîne de caractères de 0 à 7 avec un pas de 2
print(str[::-1]) # On affiche la chaîne de caractères à l'envers
print(str.lower()) # On affiche la chaîne de caractères en minuscules
print(str.upper()) # On affiche la chaîne de caractères en majuscules
print(str.capitalize()) # On affiche la chaîne de caractères avec la première lettre en majuscule
print(str.title()) # On affiche la chaîne de caractères avec la première lettre de chaque mot en majuscule
print(str.replace("Bonjour", "Bonsoir")) # On remplace le mot "Bonjour" par le mot "Bonsoir"
print(str.split(" ")) # On affiche la chaîne de caractères sous forme de liste en séparant les mots par un espace
print(str.split(" ")[0]) # On affiche le premier mot de la chaîne de caractères
print(str.split(" ")[1]) # On affiche le deuxième mot de la chaîne de caractères
print(str.split(" ")[2]) # On affiche le troisième mot de la chaîne de caractères
print(str.count("o")) # On affiche le nombre de fois que le caractère "o" apparaît dans la chaîne de caractères
print(str.count("o", 0, 7)) # On affiche le nombre de fois que le caractère "o" apparaît dans les 7 premiers caractères de la chaîne de caractères
print(str.find("o")) # On affiche la position du premier caractère "o" dans la chaîne de caractères
print(str.find("o", 0, 7)) # On affiche la position du premier caractère "o" dans les 7 premiers caractères de la chaîne de caractères
print(str.find("z")) # On affiche la position du premier caractère "z" dans la chaîne de caractères
print(str.index("o")) # On affiche la position du premier caractère "o" dans la chaîne de caractères
print(str.index("o", 0, 7)) # On affiche la position du premier caractère "o" dans les 7 premiers caractères de la chaîne de caractères
print(str.startswith("Bonjour")) # On affiche True si la chaîne de caractères commence par "Bonjour" et False sinon
print(str.endswith("!")) # On affiche True si la chaîne de caractères se termine par "!" et False sinon
print(str.islower()) # On affiche True si la chaîne de caractères est en minuscules et False sinon
print(str.isupper()) # On affiche True si la chaîne de caractères est en majuscules et False sinon
print(str.isalpha()) # On affiche True si la chaîne de caractères contient uniquement des lettres et False sinon
print(str.isalnum()) # On affiche True si la chaîne de caractères contient uniquement des lettres et des chiffres et False sinon
print(str.isnumeric()) # On affiche True si la chaîne de caractères contient uniquement des chiffres et False sinon
print(str.isdecimal()) # On affiche True si la chaîne de caractères contient uniquement des chiffres et False sinon
print(str.isspace()) # On affiche True si la chaîne de caractères contient uniquement des espaces et False sinon
print(str.istitle()) # On affiche True si la chaîne de caractères commence par une majuscule et False sinon
print(str.isprintable()) # On affiche True si la chaîne de caractères est imprimable et False sinon
print(str.strip()) # On affiche la chaîne de caractères sans les espaces au début et à la fin
print(str.lstrip()) # On affiche la chaîne de caractères sans les espaces au début
print(str.rstrip()) # On affiche la chaîne de caractères sans les espaces à la fin
print(str.center(30)) # On affiche la chaîne de caractères centrée sur 30 caractères
print(str.center(30, "-")) # On affiche la chaîne de caractères centrée sur 30 caractères avec des tirets
print(str.ljust(30)) # On affiche la chaîne de caractères alignée à gauche sur 30 caractères
print(str.ljust(30, "-")) # On affiche la chaîne de caractères alignée à gauche sur 30 caractères avec des tirets
print(str.rjust(30)) # On affiche la chaîne de caractères alignée à droite sur 30 caractères
print(str.rjust(30, "-")) # On affiche la chaîne de caractères alignée à droite sur 30 caractères avec des tirets
print(str.zfill(30)) # On affiche la chaîne de caractères avec des zéros à gauche sur 30 caractères
print(str.zfill(30)) # On affiche la chaîne de caractères avec des zéros à gauche sur 30 caractères
print(str.lstrip("#")) # On affiche la chaîne de caractères sans les caractères "#" au début
print(str.rstrip("!")) # On affiche la chaîne de caractères sans les caractères "!" à la fin
print(str.rsplit(",", 2)) # On affiche la chaîne de caractères sous forme de liste en séparant les mots par une virgule et en ne gardant que les deux derniers mots