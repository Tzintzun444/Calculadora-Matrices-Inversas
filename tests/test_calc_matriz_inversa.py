from src.calc_matriz_inversa import CalcMatrizInversa
from tests.comparador import comparar_diferencia_de_matrices
from fractions import Fraction
import pytest
import math


@pytest.mark.parametrize("matriz", [
    ([[1, 2], [3, 4], [5, 6]]),
    ([[1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24, 25, 26, 27],
      [28, 29, 30, 31, 32, 33, 34, 35, 36], [37, 38, 39, 40, 41, 42, 43, 44, 45]]),
    ([[1] * 19 for i in range(25)])
])
def test_matrices_que_no_son_cuadradas(matriz):
    assert CalcMatrizInversa.es_cuadrada(matriz) is False
    matriz_operada = CalcMatrizInversa(matriz)
    assert matriz_operada.es_invertible is False
    assert matriz_operada.matriz_inversa == []


@pytest.mark.parametrize("matriz", [
    ([[2, 4], [6, 12]]),
    ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 1, 2, 3], [15, 9, 12, 15]]),
    ([[2, 1, 4, 3, 6, 5, 8, 7], [1, 2, 3, 4, 5, 6, 7, 8], [9, 8, 7, 6, 5, 4, 3, 2], [2, 4, 6, 8, 1, 3, 5, 7],
      [3, 1, 4, 1, 5, 9, 2, 6], [8, 5, 2, 7, 4, 1, 9, 3], [6, 3, 5, 2, 8, 7, 1, 4], [31, 24, 31, 31, 34, 35, 35, 37]]),
    ([[(i + j) % 10 + 1 for j in range(15)] if i < 14 else [sum((k + j) % 10 + 1 for k in range(14)) for j in range(15)]
      for i in range(15)]),
    ([[(i * j) % 9 + 1 for j in range(18)] if i < 17 else [sum((k * j) % 9 + 1 for k in range(17)) for j in range(18)]
      for i in range(18)]),
    ([[((i + 2) * (j + 1)) % 11 + 1 for j in range(20)] if i < 19 else [sum(((k + 2) * (j + 1)) % 11 + 1 for k in
      range(19)) for j in range(20)] for i in range(20)])
])
def test_matrices_cuadradas_no_invertibles(matriz):
    matriz_operada = CalcMatrizInversa(matriz)
    assert matriz_operada.es_invertible is False
    assert matriz_operada.matriz_inversa == []


@pytest.mark.parametrize("matriz, matriz_inversa", [
    ([[1, 0], [1, 1]], [[1, 0], [-1, 1]]),
    ([[1, 0, 0, 0], [1, 1, 0, 0], [1, 2, 1, 0], [1, 3, 3, 1]], [[1, 0, 0, 0], [-1, 1, 0, 0], [1, -2, 1, 0],
                                                                [-1, 3, -3, 1]]),
    ([[1, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0], [1, 2, 1, 0, 0, 0, 0, 0], [1, 3, 3, 1, 0, 0, 0, 0],
      [1, 4, 6, 4, 1, 0, 0, 0], [1, 5, 10, 10, 5, 1, 0, 0], [1, 6, 15, 20, 15, 6, 1, 0], [1, 7, 21, 35, 35, 21, 7, 1]],
     [[1, 0, 0, 0, 0, 0, 0, 0], [-1, 1, 0, 0, 0, 0, 0, 0], [1, -2, 1, 0, 0, 0, 0, 0], [-1, 3, -3, 1, 0, 0, 0, 0],
      [1, -4, 6, -4, 1, 0, 0, 0], [-1, 5, -10, 10, -5, 1, 0, 0], [1, -6, 15, -20, 15, -6, 1, 0],
      [-1, 7, -21, 35, -35, 21, -7, 1]]),
    ([[Fraction(math.comb(i, j)) for j in range(50)] for i in range(50)],
     [[Fraction(math.comb(i, j) * ((-1)**(i - j))) for j in range(50)] for i in range(50)]),
    ([[Fraction(math.comb(i, j)) for j in range(100)] for i in range(100)],
     [[Fraction(math.comb(i, j) * ((-1)**(i - j))) for j in range(100)] for i in range(100)])
])
def test_matrices_invertibles(matriz, matriz_inversa):
    matriz_operada = CalcMatrizInversa(matriz)
    assert matriz_operada.es_invertible is True
    if matriz_operada.matriz_inversa != matriz_inversa:
        assert comparar_diferencia_de_matrices(matriz_operada.matriz_inversa, matriz_inversa,
                                               0.0000000000000000000000000000000000000000000000000000001) is True
    else:
        assert matriz_operada.matriz_inversa == matriz_inversa
