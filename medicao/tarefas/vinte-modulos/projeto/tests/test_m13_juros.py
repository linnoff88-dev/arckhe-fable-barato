import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from m13_juros import juros

def test_basico():
    assert juros(100, 0.1, 1) == 110.0
