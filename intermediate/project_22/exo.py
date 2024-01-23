class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        """ Ajoute un nouveau nœud à la fin de la liste. """
        if not self.head:
            self.head = Node(value)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)

    def display(self):
        """ Affiche tous les éléments de la liste. """
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        return elements

# Exemple d'utilisation
liste_chainee = LinkedList()
liste_chainee.append(1)
liste_chainee.append(2)
liste_chainee.append(3)

print("Éléments de la liste chaînée :", liste_chainee.display())
