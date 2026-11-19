import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from m09_hhmm import hhmm

def test_basico():
    assert hhmm(754) == '12:34'
