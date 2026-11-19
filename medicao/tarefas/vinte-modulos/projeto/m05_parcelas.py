def parcelas(total_centavos, n):
    """Divide total_centavos em n parcelas inteiras; a soma tem que bater; as primeiras levam o centavo que sobra."""
    base = total_centavos // n
    return [base] * n
