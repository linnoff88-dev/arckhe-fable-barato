#!/usr/bin/env python3
"""Checador oculto: importa cada módulo da pasta dada e roda os testes que pegam o defeito. Saída: NOTA x/20."""
import sys, importlib.util, pathlib, json
P = pathlib.Path(sys.argv[1])
CASOS = {"m01_slug": ["slug", ["slug('a  b') == 'a-b'", "slug('--Açêo!!--') == 'acao'"]], "m02_mediana": ["mediana", ["mediana([1, 2, 3, 4]) == 2.5", "mediana([5]) == 5"]], "m03_limitar": ["limitar", ["limitar(10, 0, 10) == 10", "limitar(99, 0, 10) == 10", "limitar(5, 0, 10) == 5"]], "m04_bissexto": ["bissexto", ["not bissexto(1900)", "bissexto(2000)", "not bissexto(2023)"]], "m05_parcelas": ["parcelas", ["parcelas(1000, 3) == [334, 333, 333]", "sum(parcelas(101, 4)) == 101"]], "m06_iniciais": ["iniciais", ["iniciais('Joêo da Silva') == 'JS'", "iniciais('Pedro e Paulo dos Santos') == 'PPS'"]], "m07_fatiar": ["fatiar", ["fatiar([1, 2, 3], 2) == [[1, 2], [3]]", "fatiar([], 3) == []"]], "m08_cpf_digitos": ["cpf_digitos", ["_erro(lambda: cpf_digitos('123'))"]], "m09_hhmm": ["hhmm", ["hhmm(5) == '00:05'", "hhmm(65) == '01:05'"]], "m10_unicos": ["unicos", ["unicos([3, 1, 3, 2, 1]) == [3, 1, 2]"]], "m11_porcentagem": ["porcentagem", ["porcentagem(0, 0) == 0.0", "porcentagem(1, 3) == 33.3"]], "m12_palindromo": ["palindromo", ["palindromo('A base do teto desaba')", "not palindromo('casa')", "palindromo('Ame a ema!')"]], "m13_juros": ["juros", ["juros(100, 0.1, 2) == 121.0", "juros(1000, 0.01, 12) == 1126.83"]], "m14_contar_palavras": ["contar_palavras", ["contar_palavras('Sim, sim. SIM!') == {'sim': 3}"]], "m15_primo": ["primo", ["not primo(9)", "not primo(25)", "primo(2)", "not primo(1)"]], "m16_mascara_cartao": ["mascara_cartao", ["mascara_cartao('1234 5678 9012 3456') == '**** **** **** 3456'"]], "m17_media_ponderada": ["media_ponderada", ["media_ponderada([10, 0], [3, 1]) == 7.5"]], "m18_titulo": ["titulo", ["titulo('CASA DA MOEDA') == 'Casa da Moeda'", "titulo('de volta') == 'De Volta'"]], "m19_intervalo_datas": ["dias_entre", ["dias_entre('2026-03-01', '2026-02-01') == 28"]], "m20_faixa_etaria": ["faixa", ["faixa(59) == 'adulto'", "faixa(60) == 'idoso'", "faixa(12) == 'adolescente'"]]}
def _erro(f):
    try:
        f(); return False
    except ValueError:
        return True
ok = 0
for mod, (fn, testes) in CASOS.items():
    try:
        spec = importlib.util.spec_from_file_location(mod, P / (mod + ".py")); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        g = {fn: getattr(m, fn), "_erro": _erro}
        falhas = [t for t in testes if not eval(t, g)]
    except Exception as e:
        falhas = ["erro: " + repr(e)]
    print(("OK   " if not falhas else "FALHA") + " " + mod + ("" if not falhas else "  " + "; ".join(falhas)))
    ok += not falhas
print(f"NOTA {ok}/{len(CASOS)}")
