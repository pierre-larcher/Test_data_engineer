""""Description.

Librairie de la seconde partie.
"""

from typing import Any


# EXERCICE 1


class MySet:
    """Création de l'objet MySet.
    Cet objet prend en argument des listes, celles-ci peuvent :
    - s'additionner sans inclure les doublons,
    - et soustraire de la première liste les entiers compris dans la deuxième.
    """

    def __init__(self, liste: list[int]):
        self.liste = liste

    def __repr__(self) -> str:
        """
        Exemple:
        >>> repr(MySet([1, 2, 3]))
        '[1, 2, 3]'
        """
        return repr(self.liste)

    def __iter__(self):
        """Permet de rendre itérable notre objet."""
        return iter(self.liste)

    def __add__(self, liste2: list[int]) -> set:
        """
        Exemple:
        >>> set(MySet(set([1, 2, 3]+[1, 5, 100])))
        {1, 2, 3, 100, 5}
        """
        return set(MySet(self.liste + liste2.liste))

    def __sub__(self, liste2: list[int]) -> set:
        """
        Exemple:
        >>> set(MySet(set(list(set([1, 2, 3]) - set([1, 5, 100])))))
        {2, 3}
        """
        return set(MySet(list(set(self.liste) - set(liste2.liste))))


# EXERCICE 2

maxsize = 100


def decorator_check_max_int(func):
    """Permet de forcer la fonction "add" à ne pas renvoyer de valeurs supérieures à maxsize."""

    def _new_func(a: float, b: float) -> float:
        resultat = func(a, b)
        if resultat > maxsize:
            return maxsize
        else:
            return resultat

    return _new_func


@decorator_check_max_int
def add(a: float, b: float) -> float:
    """Additionne deux flotants et renvoie la valeur "maxsize" si le résultat est supérieur."""
    return a + b


# EXERCICE 3


def ignore_exception(exception):
    """Permet d'ignorer l'exception d'une fonction et de renvoyer None si elle se déclanche."""

    def _new_func(func):
        def _wrap(*args):
            try:
                return func(*args)
            except exception:
                return None

        return _wrap

    return _new_func


@ignore_exception(ZeroDivisionError)
def div(a: float, b: float) -> float:
    """Divise deux flotants."""
    return a / b


@ignore_exception(TypeError)
def raise_something(exception):
    """Montre l'exception."""
    raise exception


# EXERCICE 4


class CacheDecorator:
    """Création de l'objet CacheDecorator.
    Cet objet permet de sauvegarder les résultat d'une fonction en fonction de ses paramètres.
    """

    def __init__(self):
        self.cache = {}

    def __call__(self, func):
        def _wrap(*a, **kw):
            if a[0] not in self.cache:
                self.cache[a[0]] = func(*a, **kw)
            return self.cache[a[0]]

        return _wrap


# EXERCICE 5


class MetaInherList:
    """Création de la Métaclasse MetaInherList.
    Cette Métaclasse permet d'intégrer à une classe une liste et de remdre celle-ci itérable.
    """

    def __init__(self, liste: list[int]):
        self.liste = liste

    def __repr__(self) -> str:
        return repr(self.liste)

    def __iter__(self):
        """Méthode pour itérer notre objet."""
        return iter(self.liste)

    def __getitem__(self, indice):
        """Applique des indices à nos éléments de liste."""
        return self.liste[indice]


class Ex:
    """Création de l'objet Ex.
    Cet objet a comme attribut x, qui vaut 4."""

    x = 4


class ForceToList(Ex, MetaInherList):
    """Création de l'objet ForceToList.
    Attribut la liste intégrée de MetaInherList à notre objet."""

    liste = MetaInherList
