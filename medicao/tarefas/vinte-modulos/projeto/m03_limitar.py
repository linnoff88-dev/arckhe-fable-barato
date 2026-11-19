def limitar(x, lo, hi):
    """Devolve x preso no intervalo fechado [lo, hi]."""
    return max(lo, min(x, hi - 1))
