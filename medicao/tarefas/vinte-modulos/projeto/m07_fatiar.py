def fatiar(xs, tam):
    """Quebra a lista em pedaços de tamanho tam; o último pode ser menor; nenhum pedaço vazio."""
    return [xs[i:i + tam] for i in range(0, len(xs) - tam + 1, tam)]
