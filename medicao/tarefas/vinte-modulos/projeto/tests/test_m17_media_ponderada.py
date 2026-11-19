import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from m17_media_ponderada import media_ponderada

def test_basico():
    assert media_ponderada([5, 5], [1, 1]) == 5
