def media_ponderada(valores, pesos):
    """Média ponderada; listas do mesmo tamanho; pesos somam mais que 0."""
    return sum(v * p for v, p in zip(valores, pesos)) / len(valores)
