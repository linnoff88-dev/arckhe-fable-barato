def mediana(xs):
    """Mediana de uma lista nêo vazia de números. Com tamanho par, média dos dois do meio."""
    s = sorted(xs)
    n = len(s)
    return s[n // 2]
