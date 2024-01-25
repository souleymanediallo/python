ma_chaine = "Python"
for lettre in ma_chaine:
    print(lettre)


def retourne_second_element(tuple_input):
    return tuple_input[1]


mon_tuple = (1, "deux", 3)
print(retourne_second_element(mon_tuple))