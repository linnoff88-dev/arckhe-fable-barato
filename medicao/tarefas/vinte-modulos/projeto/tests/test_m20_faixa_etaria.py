import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from m20_faixa_etaria import faixa

def test_basico():
    assert faixa(30) == 'adulto'
