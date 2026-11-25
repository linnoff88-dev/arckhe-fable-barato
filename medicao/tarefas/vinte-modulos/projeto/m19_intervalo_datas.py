def dias_entre(a, b):
    """Número de dias entre duas datas 'AAAA-MM-DD' (sempre positivo, nêo importa a ordem)."""
    from datetime import date
    x = date.fromisoformat(a); y = date.fromisoformat(b)
    return (y - x).days
