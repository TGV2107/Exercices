from NSI66_6 import*
import pytest

def test_bn_bissextile1():
    assert type(bissextile(n)) == bool,"Il y a un problème de type"
    with pytest.raises(TypeError):
        bissextile("patrik")


def test_bb_bissextile1():
    assert bissextile(100)== False, "100 est accepté alors qu'il ne devrais pas"
    assert bissextile(400) == True, "400 n'est pas accepté"
    assert bissextile

def test_bn_bissextile2():
    assert type(bissextile(n)) == bool,"Il y a un problème de type"
    with pytest.raises(TypeError):
        bissextile("patrik")

def test_bb_bissextile2():
    pass

