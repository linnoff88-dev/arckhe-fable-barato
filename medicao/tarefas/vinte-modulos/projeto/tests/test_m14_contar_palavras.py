import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from m14_contar_palavras import contar_palavras

def test_basico():
    assert contar_palavras('a b a') == {'a': 2, 'b': 1}
