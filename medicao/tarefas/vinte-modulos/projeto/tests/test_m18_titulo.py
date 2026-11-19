import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from m18_titulo import titulo

def test_basico():
    assert titulo('ana') == 'Ana'
