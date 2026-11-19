import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from m03_limitar import limitar

def test_basico():
    assert limitar(-5, 0, 10) == 0
