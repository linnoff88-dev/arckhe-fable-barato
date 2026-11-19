import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from m07_fatiar import fatiar

def test_basico():
    assert fatiar([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]
