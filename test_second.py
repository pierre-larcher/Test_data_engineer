"""Description.

Tests automatiques de la seconde partie.
"""

from lib_second import MySet, add, div, raise_something, CacheDecorator, ForceToList
import pytest


# EXERCICE 1


def test_my_set():
    a = MySet([1, 2, 3])
    b = MySet([1, 5, 100])
    assert a + b == {1, 2, 3, 100, 5}
    assert a - b == {2, 3}


# EXERCICE 2


maxsize = 100


def test_max_int():
    assert add(5, 30) == 35
    assert add(maxsize, 1) == maxsize


# EXERCICE 3


def test_ignore_exception():
    assert div(10, 2) == 5
    assert div(10, 0) is None
    assert raise_something(TypeError) is None
    with pytest.raises(NotImplementedError):
        raise_something(NotImplementedError)


# EXERCICE 4


def test_cache_initialisation():
    attributs = CacheDecorator()
    assert attributs.cache == {}


def test_cache_appelation():
    attributs = CacheDecorator()
    assert attributs.__call__ != {}


# EXERCICE 5


def test_meta_list():
    test = ForceToList([1, 2])
    assert test[1] == 2
    assert test.x == 4
