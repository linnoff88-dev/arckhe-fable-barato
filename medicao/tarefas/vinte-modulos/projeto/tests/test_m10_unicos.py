import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from m10_unicos import unicos

def test_basico():
    assert sorted(unicos([1, 1, 2])) == [1, 2]
