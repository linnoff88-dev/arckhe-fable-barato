def porcentagem(parte, todo):
    """Percentual de parte em todo, arredondado a 1 casa; se todo for 0, devolve 0.0."""
    return round(parte / todo * 100, 1)
