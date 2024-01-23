import page_66_6
import pytest


def test_bn_bissextile1():
    assert type(page_66_6.bissextile(4)) == bool, "bissextile 1 ne revoie pas un booléen"
    with pytest.raises(TypeError):
        page_66_6.bissextile("Quentin est un noob")

def test_bb_bissextile1():
    assert page_66_6.bissextile(4) == True, "4 n'est pas correcte dans bis1"
    assert page_66_6.bissextile(100) == False, "100 n'est pas correcte dans bis1"
    assert page_66_6.bissextile(400) == True, "400 n'est pas correcte dans bis1"
    assert page_66_6.bissextile(1) == False, "1 n'est pas correcte dans bis1"

def test_bn_bissextile2():
    assert type(page_66_6.bissextile2(4)) == bool, "bissextile 2 ne revoie pas un booléen"
    with pytest.raises(TypeError):
        page_66_6.bissextile2("Quentin est un noob")

def test_bb_bissextile2():
    assert page_66_6.bissextile2(4) == True, "4 n'est pas correcte dans bis2"
    assert page_66_6.bissextile2(100) == False, "100 n'est pas correcte dans bis2"
    assert page_66_6.bissextile2(400) == True, "400 n'est pas correcte dans bis2"
    assert page_66_6.bissextile2(1) == False, "1 n'est pas correcte dans bis2"