def mascara_cartao(numero):
    """Mostra só os 4 últimos dígitos: '**** **** **** 1234'. Ignora espaços na entrada."""
    d = numero.replace(' ', '')
    return '**** **** **** ' + d[:4]
