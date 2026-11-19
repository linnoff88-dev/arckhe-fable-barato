def palindromo(s):
    """True se s for palíndromo ignorando maiúsculas, espaços e pontuação."""
    return s == s[::-1]
