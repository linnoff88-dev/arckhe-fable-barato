#!/usr/bin/env python3
"""Gera a tarefa GRANDE da medição dos 3 jeitos: 20 módulos independentes, cada um com 1 defeito plantado.
projeto/ = o que o modelo vê (código com defeito + docstring com a regra + 1 teste fraco por módulo).
oculto/checar.py = checador que o modelo não vê (testes que pegam cada defeito). Nota = módulos certos / 20.
Uso: python3 gerar.py  (recria projeto/ e oculto/ ao lado deste arquivo)"""
import pathlib, shutil, textwrap, json

AQUI = pathlib.Path(__file__).resolve().parent
M = [
 ("slug", "def slug(texto):\n    \"\"\"Minúsculas, troca qualquer sequência de não-alfanuméricos por um único '-', sem '-' nas pontas. Acentos são removidos (ç->c, ã->a).\"\"\"\n    import re, unicodedata\n    t = unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode()\n    t = re.sub(r'[^a-zA-Z0-9]', '-', t.lower())\n    return t.strip('-')\n",
  "assert slug('Olá Mundo') == 'ola-mundo'", ["slug('a  b') == 'a-b'", "slug('--Ação!!--') == 'acao'"]),
 ("mediana", "def mediana(xs):\n    \"\"\"Mediana de uma lista não vazia de números. Com tamanho par, média dos dois do meio.\"\"\"\n    s = sorted(xs)\n    n = len(s)\n    return s[n // 2]\n",
  "assert mediana([3, 1, 2]) == 2", ["mediana([1, 2, 3, 4]) == 2.5", "mediana([5]) == 5"]),
 ("limitar", "def limitar(x, lo, hi):\n    \"\"\"Devolve x preso no intervalo fechado [lo, hi].\"\"\"\n    return max(lo, min(x, hi - 1))\n",
  "assert limitar(-5, 0, 10) == 0", ["limitar(10, 0, 10) == 10", "limitar(99, 0, 10) == 10", "limitar(5, 0, 10) == 5"]),
 ("bissexto", "def bissexto(ano):\n    \"\"\"Ano bissexto no calendário gregoriano.\"\"\"\n    return ano % 4 == 0\n",
  "assert bissexto(2024)", ["not bissexto(1900)", "bissexto(2000)", "not bissexto(2023)"]),
 ("parcelas", "def parcelas(total_centavos, n):\n    \"\"\"Divide total_centavos em n parcelas inteiras; a soma tem que bater; as primeiras levam o centavo que sobra.\"\"\"\n    base = total_centavos // n\n    return [base] * n\n",
  "assert parcelas(900, 3) == [300, 300, 300]", ["parcelas(1000, 3) == [334, 333, 333]", "sum(parcelas(101, 4)) == 101"]),
 ("iniciais", "def iniciais(nome):\n    \"\"\"Iniciais em maiúsculas das palavras do nome, ignorando 'da', 'de', 'do', 'das', 'dos' e 'e'.\"\"\"\n    return ''.join(p[0].upper() for p in nome.split())\n",
  "assert iniciais('ana maria') == 'AM'", ["iniciais('João da Silva') == 'JS'", "iniciais('Pedro e Paulo dos Santos') == 'PPS'"]),
 ("fatiar", "def fatiar(xs, tam):\n    \"\"\"Quebra a lista em pedaços de tamanho tam; o último pode ser menor; nenhum pedaço vazio.\"\"\"\n    return [xs[i:i + tam] for i in range(0, len(xs) - tam + 1, tam)]\n",
  "assert fatiar([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]", ["fatiar([1, 2, 3], 2) == [[1, 2], [3]]", "fatiar([], 3) == []"]),
 ("cpf_digitos", "def cpf_digitos(cpf):\n    \"\"\"Recebe CPF com ou sem pontuação e devolve só os 11 dígitos como string; se não tiver 11 dígitos, levanta ValueError.\"\"\"\n    d = ''.join(c for c in cpf if c.isdigit())\n    return d\n",
  "assert cpf_digitos('123.456.789-09') == '12345678909'", ["_erro(lambda: cpf_digitos('123'))"]),
 ("hhmm", "def hhmm(minutos):\n    \"\"\"Formata minutos (0 a 5999) como 'HH:MM' com dois dígitos em cada parte.\"\"\"\n    return f'{minutos // 60}:{minutos % 60:02d}'\n",
  "assert hhmm(754) == '12:34'", ["hhmm(5) == '00:05'", "hhmm(65) == '01:05'"]),
 ("unicos", "def unicos(xs):\n    \"\"\"Remove repetidos mantendo a ordem da primeira aparição.\"\"\"\n    return list(set(xs))\n",
  "assert sorted(unicos([1, 1, 2])) == [1, 2]", ["unicos([3, 1, 3, 2, 1]) == [3, 1, 2]"]),
 ("porcentagem", "def porcentagem(parte, todo):\n    \"\"\"Percentual de parte em todo, arredondado a 1 casa; se todo for 0, devolve 0.0.\"\"\"\n    return round(parte / todo * 100, 1)\n",
  "assert porcentagem(1, 4) == 25.0", ["porcentagem(0, 0) == 0.0", "porcentagem(1, 3) == 33.3"]),
 ("palindromo", "def palindromo(s):\n    \"\"\"True se s for palíndromo ignorando maiúsculas, espaços e pontuação.\"\"\"\n    return s == s[::-1]\n",
  "assert palindromo('ovo')", ["palindromo('Socorram-me, subi no ônibus em Marrocos') is False or True", "palindromo('A base do teto desaba')", "not palindromo('casa')"]),
 ("juros", "def juros(capital, taxa_mes, meses):\n    \"\"\"Montante com juros COMPOSTOS, arredondado a 2 casas. taxa_mes em fração (0.01 = 1%).\"\"\"\n    return round(capital * (1 + taxa_mes * meses), 2)\n",
  "assert juros(100, 0.1, 1) == 110.0", ["juros(100, 0.1, 2) == 121.0", "juros(1000, 0.01, 12) == 1126.83"]),
 ("contar_palavras", "def contar_palavras(texto):\n    \"\"\"Dicionário palavra->contagem, sem diferenciar maiúsculas, ignorando pontuação nas pontas da palavra.\"\"\"\n    c = {}\n    for p in texto.split():\n        c[p] = c.get(p, 0) + 1\n    return c\n",
  "assert contar_palavras('a b a') == {'a': 2, 'b': 1}", ["contar_palavras('Sim, sim. SIM!') == {'sim': 3}"]),
 ("primo", "def primo(n):\n    \"\"\"True se n for primo (n inteiro).\"\"\"\n    if n < 2:\n        return False\n    for d in range(2, int(n ** 0.5)):\n        if n % d == 0:\n            return False\n    return True\n",
  "assert primo(7)", ["not primo(9)", "not primo(25)", "primo(2)", "not primo(1)"]),
 ("mascara_cartao", "def mascara_cartao(numero):\n    \"\"\"Mostra só os 4 últimos dígitos: '**** **** **** 1234'. Ignora espaços na entrada.\"\"\"\n    d = numero.replace(' ', '')\n    return '**** **** **** ' + d[:4]\n",
  "assert mascara_cartao('1111 1111 1111 1111') == '**** **** **** 1111'", ["mascara_cartao('1234 5678 9012 3456') == '**** **** **** 3456'"]),
 ("media_ponderada", "def media_ponderada(valores, pesos):\n    \"\"\"Média ponderada; listas do mesmo tamanho; pesos somam mais que 0.\"\"\"\n    return sum(v * p for v, p in zip(valores, pesos)) / len(valores)\n",
  "assert media_ponderada([5, 5], [1, 1]) == 5", ["media_ponderada([10, 0], [3, 1]) == 7.5"]),
 ("titulo", "def titulo(s):\n    \"\"\"Primeira letra de cada palavra maiúscula e o resto minúsculo; 'de', 'da', 'do' ficam minúsculas, exceto como primeira palavra.\"\"\"\n    return ' '.join(p.capitalize() for p in s.split())\n",
  "assert titulo('ana') == 'Ana'", ["titulo('CASA DA MOEDA') == 'Casa da Moeda'", "titulo('de volta') == 'De Volta'"]),
 ("intervalo_datas", "def dias_entre(a, b):\n    \"\"\"Número de dias entre duas datas 'AAAA-MM-DD' (sempre positivo, não importa a ordem).\"\"\"\n    from datetime import date\n    x = date.fromisoformat(a); y = date.fromisoformat(b)\n    return (y - x).days\n",
  "assert dias_entre('2026-01-01', '2026-01-31') == 30", ["dias_entre('2026-03-01', '2026-02-01') == 28"]),
 ("faixa_etaria", "def faixa(idade):\n    \"\"\"'crianca' até 11, 'adolescente' de 12 a 17, 'adulto' de 18 a 59, 'idoso' a partir de 60.\"\"\"\n    if idade < 12:\n        return 'crianca'\n    if idade < 18:\n        return 'adolescente'\n    if idade < 59:\n        return 'adulto'\n    return 'idoso'\n",
  "assert faixa(30) == 'adulto'", ["faixa(59) == 'adulto'", "faixa(60) == 'idoso'", "faixa(12) == 'adolescente'"]),
]
# corrige um teste que ficou frouxo de propósito no palíndromo
M[11] = (M[11][0], M[11][1], M[11][2], ["palindromo('A base do teto desaba')", "not palindromo('casa')", "palindromo('Ame a ema!')"])

proj, ocul = AQUI / "projeto", AQUI / "oculto"
for d in (proj, ocul):
    shutil.rmtree(d, ignore_errors=True); d.mkdir()
(proj / "tests").mkdir()
for i, (nome, codigo, vis, _) in enumerate(M, 1):
    mod = f"m{i:02d}_{nome}"
    (proj / f"{mod}.py").write_text(codigo)
    fn = codigo.split("def ")[1].split("(")[0]
    (proj / "tests" / f"test_{mod}.py").write_text(f"import sys, pathlib\nsys.path.insert(0, str(pathlib.Path(__file__).parent.parent))\nfrom {mod} import {fn}\n\ndef test_basico():\n    {vis}\n")
(proj / "LEIAME.md").write_text("# 20 utilitários\n\nCada módulo mXX_*.py tem uma função com a regra na docstring. Testes básicos em tests/ (rodar: python3 -m pytest -q tests ou python3 tests/test_*.py).\n")
casos = {f"m{i:02d}_{n}": (c.split('def ')[1].split('(')[0], h) for i, (n, c, _, h) in enumerate(M, 1)}
(ocul / "checar.py").write_text(textwrap.dedent(f'''\
    #!/usr/bin/env python3
    """Checador oculto: importa cada módulo da pasta dada e roda os testes que pegam o defeito. Saída: NOTA x/20."""
    import sys, importlib.util, pathlib, json
    P = pathlib.Path(sys.argv[1])
    CASOS = {json.dumps(casos, ensure_ascii=False)}
    def _erro(f):
        try:
            f(); return False
        except ValueError:
            return True
    ok = 0
    for mod, (fn, testes) in CASOS.items():
        try:
            spec = importlib.util.spec_from_file_location(mod, P / (mod + ".py")); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
            g = {{fn: getattr(m, fn), "_erro": _erro}}
            falhas = [t for t in testes if not eval(t, g)]
        except Exception as e:
            falhas = ["erro: " + repr(e)]
        print(("OK   " if not falhas else "FALHA") + " " + mod + ("" if not falhas else "  " + "; ".join(falhas)))
        ok += not falhas
    print(f"NOTA {{ok}}/{{len(CASOS)}}")
'''))
(AQUI / "pedido.txt").write_text("Este projeto tem 20 módulos independentes (mXX_*.py). Cada um tem a regra na docstring, e vários não seguem a regra. Revise e corrija TODOS os módulos para seguirem exatamente a docstring. Os testes em tests/ são só básicos.\n")
print("ok:", len(M), "módulos")
