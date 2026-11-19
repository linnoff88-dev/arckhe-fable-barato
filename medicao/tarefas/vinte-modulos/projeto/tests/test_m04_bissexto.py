import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from m04_bissexto import bissexto

def test_basico():
    assert bissexto(2024)
