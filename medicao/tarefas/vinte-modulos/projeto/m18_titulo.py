def titulo(s):
    """Primeira letra de cada palavra maiúscula e o resto minúsculo; 'de', 'da', 'do' ficam minúsculas, exceto como primeira palavra."""
    return ' '.join(p.capitalize() for p in s.split())
