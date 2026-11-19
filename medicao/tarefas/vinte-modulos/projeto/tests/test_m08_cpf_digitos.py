import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from m08_cpf_digitos import cpf_digitos

def test_basico():
    assert cpf_digitos('123.456.789-09') == '12345678909'
