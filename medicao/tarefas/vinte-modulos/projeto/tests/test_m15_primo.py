import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from m15_primo import primo

def test_basico():
    assert primo(7)
