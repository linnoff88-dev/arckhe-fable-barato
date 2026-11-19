import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from m01_slug import slug

def test_basico():
    assert slug('Olá Mundo') == 'ola-mundo'
