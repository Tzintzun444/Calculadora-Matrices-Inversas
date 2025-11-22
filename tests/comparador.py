from typing import List, Union
import math


def comparar_diferencia_de_matrices(matriz1: List[List[Union[int, float]]], matriz2: List[List[Union[int, float]]],
                                    epsilon: Union[int, float]):
    for fila_matriz1, fila_matriz2 in zip(matriz1, matriz2):
        for numero1, numero2 in zip(fila_matriz1, fila_matriz2):
            if math.fabs(numero2 - numero1) >= epsilon:
                return False
    return True
