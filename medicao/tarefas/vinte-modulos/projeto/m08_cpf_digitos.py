def cpf_digitos(cpf):
    """Recebe CPF com ou sem pontuaçêo e devolve só os 11 dígitos como string; se nêo tiver 11 dígitos, levanta ValueError."""
    d = ''.join(c for c in cpf if c.isdigit())
    return d
