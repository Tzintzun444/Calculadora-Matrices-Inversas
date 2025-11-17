from typing import Union, List


class CalcMatrizInversa:

    def __init__(self):
        pass

    @staticmethod
    def es_cuadrada(matriz: List[List[Union[int, float]]]):
        filas = len(matriz)
        for fila in matriz:
            if len(fila) != filas:
                return False
        return True

    @staticmethod
    def sin_fila_columna_0(matriz: List[List[Union[int, float]]]):
        dimension = len(matriz)
        if [0] * dimension in matriz:
            return False
        for columna in range(dimension):
            if [0] * dimension == [fila[columna] for fila in matriz]:
                return False
        return True

