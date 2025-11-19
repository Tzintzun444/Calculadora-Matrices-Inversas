from typing import Union, List


class CalcMatrizInversa:

    def __init__(self, matriz: List[List[Union[int, float]]]):
        self._matriz = matriz
        self._matriz_inversa = None
        self._es_invertible = None
        self.escalonar_matriz()

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

    @staticmethod
    def multiplicar_renglon_por_escalar(fila: List[int], k: Union[int, float]):
        return [numero * k for numero in fila]

    @staticmethod
    def sumar_fila_a_otro(fila1: List[int], fila2: List[int]):
        return [num1 + num2 for num1, num2 in zip(fila1, fila2)]

    @classmethod
    def multiplicar_fila_y_sumarla(cls, fila_a_multiplicar: List[int], k: Union[int, float],
                                   fila_a_sumar: List[int]):
        return cls.sumar_fila_a_otro(cls.multiplicar_renglon_por_escalar(fila_a_multiplicar, k),
                                     fila_a_sumar)

    @staticmethod
    def intercambiar_filas(matriz: List[List[Union[int, float]]], fila1: int, fila2: int):
        matriz_intercambiada = []
        for fila in range(len(matriz)):
            if fila == fila1:
                matriz_intercambiada.append(matriz[fila2])
            elif fila == fila2:
                matriz_intercambiada.append(matriz[fila1])
            else:
                matriz_intercambiada.append(matriz[fila])
        return matriz_intercambiada

    @staticmethod
    def generar_matriz_identidad(dimension: int):
        matriz_identidad = [[0] * dimension for _ in range(dimension)]
        for i in range(dimension):
            matriz_identidad[i][i] += 1
        return matriz_identidad

    @staticmethod
    def transponer_matriz(matriz: List[List[Union[int, float]]]):
        matriz_transpuesta = [[] for _ in range(len(matriz))]
        for fila in matriz:
            for indice in range(len(matriz)):
                matriz_transpuesta[indice].append(fila[indice])
        return matriz_transpuesta

    def escalonar_matriz(self):
        if not self.es_cuadrada(self._matriz):
            self._es_invertible = False
            self._matriz_inversa = []
        matriz_escalonada = self._matriz.copy()
        matriz_inversa = self.generar_matriz_identidad(len(matriz_escalonada))
        pivote = 0
        while pivote < len(matriz_escalonada) - 1:
            if not self.sin_fila_columna_0(matriz_escalonada):
                self._es_invertible = False
                self._matriz_inversa = []
            while matriz_escalonada[pivote][pivote] == 0:
                matriz_inversa = self.intercambiar_filas(matriz_inversa, 0, len(matriz_inversa) - 1)
                matriz_escalonada = self.intercambiar_filas(matriz_escalonada, 0, len(matriz_escalonada) - 1)
            matriz_inversa[pivote] = self.multiplicar_renglon_por_escalar(matriz_inversa[pivote],
                                                                          matriz_escalonada[pivote][pivote] ** - 1)
            matriz_escalonada[pivote] = self.multiplicar_renglon_por_escalar(matriz_escalonada[pivote],
                                                                             matriz_escalonada[pivote][pivote] ** - 1)
            for i in range(len(matriz_escalonada) - 1 - pivote):
                matriz_inversa[i + 1 + pivote] = self.multiplicar_fila_y_sumarla(matriz_inversa[pivote],
                                                                                 - matriz_escalonada[i + 1 + pivote][
                                                                                       pivote],
                                                                                 matriz_inversa[i + 1 + pivote])
                matriz_escalonada[i + 1 + pivote] = self.multiplicar_fila_y_sumarla(matriz_escalonada[pivote],
                                                                                    - matriz_escalonada[i + 1 + pivote][pivote],
                                                                                    matriz_escalonada[i + 1 + pivote])
            pivote += 1
        while pivote > 0:
            if not self.sin_fila_columna_0(matriz_escalonada):
                self._es_invertible = False
                self._matriz_inversa = []
            # while matriz_escalonada[pivote][pivote] == 0:
            #     matriz_escalonada = self.intercambiar_filas(matriz_escalonada, 0, len(matriz_escalonada) - 1)
            matriz_inversa[pivote] = self.multiplicar_renglon_por_escalar(matriz_inversa[pivote],
                                                                          matriz_escalonada[pivote][pivote] ** - 1)
            matriz_escalonada[pivote] = self.multiplicar_renglon_por_escalar(matriz_escalonada[pivote],
                                                                             matriz_escalonada[pivote][pivote] ** - 1)
            for i in range(pivote):
                matriz_inversa[pivote - i - 1] = self.multiplicar_fila_y_sumarla(matriz_inversa[pivote],
                                                                                 - matriz_escalonada[pivote - i - 1][
                                                                                       pivote],
                                                                                 matriz_inversa[pivote - i - 1])
                matriz_escalonada[pivote - i - 1] = self.multiplicar_fila_y_sumarla(matriz_escalonada[pivote],
                                                                                    - matriz_escalonada[pivote - i - 1][pivote],
                                                                                    matriz_escalonada[pivote - i - 1])
            pivote -= 1
        self._es_invertible = True
        self._matriz_inversa = matriz_inversa


matriz = CalcMatrizInversa([[10, 20], [10, 10]])
