class ComparadorService:
    """Clase encargada exclusivamente de la lógica de comparación."""

    @staticmethod
    def comparar_enteros(x: int, y: int) -> str:
        if x > y:
            return f"{x} es mayor que {y}"
        elif x < y:
            return f"{x} es menor que {y}"
        return f"{x} es igual a {y}"
