""""Description.

Librairie de la première partie.
"""


# EXERCICE 1


def exercise_one():
    """Imprime chaque nombre de 1 à 100 et renvoie les multiples de 3 comme 'Three',
    ceux de 5 comme 'Five' et ceux de 3 et de 5 comme 'ThreeFive'."""
    for nombre in range(1, 101):
        if nombre % 3 == 0 and nombre % 5 != 0:
            print("Three")
        elif nombre % 5 == 0 and nombre % 5 != 0:
            print("Five")
        elif nombre % 3 == 0 and nombre % 5 == 0:
            print("ThreeFive")
        else:
            print(nombre)


# EXERCICE 2


def find_missing_nb(arr: list[int]) -> int:
    """Permet de trouver le nombre manquant d'une liste comprise entre 1 et n."""
    n = len(arr) + 2
    for nombre in range(1, n):
        if nombre in arr:
            pass
        else:
            return nombre


# EXERCICE 3


def sort_positive_element(arr: list[int]) -> list[int]:
    """Permet de trier une liste de nombre sans changer la position des nombres négatifs.
    Cette fonction fonctionne même avec des doublons.
    """
    copy_liste = [element for element in arr if element > 0]
    for index, element in enumerate(arr):
        if element < 0:
            pass
        else:
            arr[index] = min(copy_liste)
            copy_liste.remove(min(copy_liste))
    return arr
