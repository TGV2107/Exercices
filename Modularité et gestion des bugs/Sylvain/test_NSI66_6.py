from NSI66_6 import*
import pytest

def test_bn_bissextile1():
    assert type(bissextile(100)) == bool,"Il y a un problème de type"
    with pytest.raises(TypeError):
        bissextile("patrik")


def test_bb_bissextile1():
    assert bissextile(100)== False, "100 est accepté alors qu'il ne devrais pas"
    assert bissextile(400) == True, "400 n'est pas accepté"
    assert bissextile(4) == True, "4 n'est pas accepté"
    assert bissextile(1) == False, "1 ne doit pas être bissextile"


def test_bn_bissextile2():
    assert type(bissextile(100)) == bool,"Il y a un problème de type"
    with pytest.raises(TypeError):
        bissextile("patrik")

def test_bb_bissextile2():
    assert bis(100)== False, "100 est accepté alors qu'il ne devrais pas"
    assert bis(4) == True, "4 n'est pas accepté"
    assert bis(1) == False, "1 ne doit pas être bissextile"
    assert bis(400) == True, "400 n'est pas accepté"

