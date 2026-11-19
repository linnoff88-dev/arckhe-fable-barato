def hhmm(minutos):
    """Formata minutos (0 a 5999) como 'HH:MM' com dois dígitos em cada parte."""
    return f'{minutos // 60}:{minutos % 60:02d}'
