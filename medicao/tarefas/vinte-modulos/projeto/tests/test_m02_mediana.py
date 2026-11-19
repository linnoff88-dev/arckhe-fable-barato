import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from m02_mediana import mediana

def test_basico():
    assert mediana([3, 1, 2]) == 2
