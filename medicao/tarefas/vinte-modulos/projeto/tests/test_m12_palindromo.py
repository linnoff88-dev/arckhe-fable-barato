import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from m12_palindromo import palindromo

def test_basico():
    assert palindromo('ovo')
