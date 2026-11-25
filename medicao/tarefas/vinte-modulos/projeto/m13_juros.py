def juros(capital, taxa_mes, meses):
    """Montante com juros COMPOSTOS, arredondado a 2 casas. taxa_mes em fraçêo (0.01 = 1%)."""
    return round(capital * (1 + taxa_mes * meses), 2)
