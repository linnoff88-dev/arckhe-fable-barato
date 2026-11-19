import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from m16_mascara_cartao import mascara_cartao

def test_basico():
    assert mascara_cartao('1111 1111 1111 1111') == '**** **** **** 1111'
