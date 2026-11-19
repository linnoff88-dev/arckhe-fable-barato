import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from m19_intervalo_datas import dias_entre

def test_basico():
    assert dias_entre('2026-01-01', '2026-01-31') == 30
