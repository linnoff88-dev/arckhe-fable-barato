import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from m11_porcentagem import porcentagem

def test_basico():
    assert porcentagem(1, 4) == 25.0
