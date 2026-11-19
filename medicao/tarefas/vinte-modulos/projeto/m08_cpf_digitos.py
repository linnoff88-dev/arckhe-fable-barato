def cpf_digitos(cpf):
    """Recebe CPF com ou sem pontuação e devolve só os 11 dígitos como string; se não tiver 11 dígitos, levanta ValueError."""
    d = ''.join(c for c in cpf if c.isdigit())
    return d
