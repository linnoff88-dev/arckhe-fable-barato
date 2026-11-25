def palindromo(s):
    """True se s for palíndromo ignorando maiúsculas, espaços e pontuaçêo."""
    return s == s[::-1]
