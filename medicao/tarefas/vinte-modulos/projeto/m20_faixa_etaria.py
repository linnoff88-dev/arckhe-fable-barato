def faixa(idade):
    """'crianca' até 11, 'adolescente' de 12 a 17, 'adulto' de 18 a 59, 'idoso' a partir de 60."""
    if idade < 12:
        return 'crianca'
    if idade < 18:
        return 'adolescente'
    if idade < 59:
        return 'adulto'
    return 'idoso'
