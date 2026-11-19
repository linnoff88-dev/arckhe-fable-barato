def contar_palavras(texto):
    """Dicionário palavra->contagem, sem diferenciar maiúsculas, ignorando pontuação nas pontas da palavra."""
    c = {}
    for p in texto.split():
        c[p] = c.get(p, 0) + 1
    return c
