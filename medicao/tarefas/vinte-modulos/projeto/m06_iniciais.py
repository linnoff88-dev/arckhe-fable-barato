def iniciais(nome):
    """Iniciais em maiúsculas das palavras do nome, ignorando 'da', 'de', 'do', 'das', 'dos' e 'e'."""
    return ''.join(p[0].upper() for p in nome.split())
