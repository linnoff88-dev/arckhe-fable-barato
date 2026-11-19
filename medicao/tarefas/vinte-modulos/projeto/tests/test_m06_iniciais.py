import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from m06_iniciais import iniciais

def test_basico():
    assert iniciais('ana maria') == 'AM'
