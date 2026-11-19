import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from m05_parcelas import parcelas

def test_basico():
    assert parcelas(900, 3) == [300, 300, 300]
