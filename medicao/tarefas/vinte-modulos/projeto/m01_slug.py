def slug(texto):
    """Minúsculas, troca qualquer sequência de não-alfanuméricos por um único '-', sem '-' nas pontas. Acentos são removidos (ç->c, ã->a)."""
    import re, unicodedata
    t = unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode()
    t = re.sub(r'[^a-zA-Z0-9]', '-', t.lower())
    return t.strip('-')
