import pytest
from login import encript

def test_encript ():
    assert encript("10100") == "bcSKqUka5Pw8IPEe80WWlD8MIxQ="

@pytest.mark.parametrize(
    "palabra, letras",[
        ("10100","bcSKqUka5Pw8IPEe80WWlD8MIxQ=")
    ]
) 
def test_encript_multiple(palabra, letras):
    assert encript(palabra) == letras