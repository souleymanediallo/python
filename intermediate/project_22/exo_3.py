str = "Bonjour tout lemonde!" # On définit une variable str qui contient une chaîne de caractères
sep = "-" # On définit une variable sep qui contient une chaîne de caractères
print(sep.join(str)) # On affiche la chaîne de caractères avec le séparateur entre chaque caractère
print(sep.join(str.split(" "))) # On affiche la chaîne de caractères avec le séparateur entre chaque mot
print(sep.join(str.split(" ")[0])) # On affiche le premier mot de la chaîne de caractères avec le séparateur entre chaque caractère
print(sep.join(str.split(" ")[1])) # On affiche le deuxième mot de la chaîne de caractères avec le séparateur entre chaque caractère
