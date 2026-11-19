def primo(n):
    """True se n for primo (n inteiro)."""
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5)):
        if n % d == 0:
            return False
    return True
