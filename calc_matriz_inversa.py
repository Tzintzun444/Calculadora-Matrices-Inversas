from typing import Union, List


class CalcMatrizInversa:

    def __init__(self, matriz: List[List[Union[int, float]]]):
        self._matriz = matriz
        self._matriz_inversa = None
        self._es_invertible = None
        self.obtener_matriz_inversa()

    @property
    def matriz(self) -> List[List[Union[int, float]]]:
        return self._matriz

    @property
    def matriz_inversa(self) -> List[List[Union[int, float]]]:
        return self._matriz_inversa

    @property
    def es_invertible(self) -> bool:
        return self._es_invertible

    @staticmethod
    def es_cuadrada(matriz: List[List[Union[int, float]]]) -> bool:
        filas = len(matriz)
        for fila in matriz:
            if len(fila) != filas:
                return False
        return True

    @staticmethod
    def sin_fila_columna_0(matriz: List[List[Union[int, float]]]) -> bool:
        dimension = len(matriz)
        if [0] * dimension in matriz:
            return False
        for columna in range(dimension):
            if [0] * dimension == [fila[columna] for fila in matriz]:
                return False
        return True

    @staticmethod
    def multiplicar_fila_por_escalar(fila: List[int], k: Union[int, float]) -> List[Union[int, float]]:
        return [numero * k for numero in fila]

    @staticmethod
    def sumar_fila_a_otro(fila1: List[int], fila2: List[int]) -> List[Union[int, float]]:
        return [num1 + num2 for num1, num2 in zip(fila1, fila2)]

    @classmethod
    def multiplicar_fila_y_sumarla(cls, fila_a_multiplicar: List[int], k: Union[int, float],
                                   fila_a_sumar: List[int]) -> List[Union[int, float]]:
        return cls.sumar_fila_a_otro(cls.multiplicar_fila_por_escalar(fila_a_multiplicar, k),
                                     fila_a_sumar)

    @staticmethod
    def intercambiar_filas(matriz: List[List[Union[int, float]]], num_fila: int) -> List[List[Union[int, float]]]:
        fila_a_mover = matriz[num_fila].copy()
        matriz.pop(num_fila)
        matriz.append(fila_a_mover)
        return matriz

    @staticmethod
    def generar_matriz_identidad(dimension: int) -> List[List[Union[int, float]]]:
        matriz_identidad = [[0] * dimension for _ in range(dimension)]
        for i in range(dimension):
            matriz_identidad[i][i] += 1
        return matriz_identidad

    def obtener_matriz_inversa(self) -> None:
        if not self.es_cuadrada(self._matriz):
            self._es_invertible = False
            self._matriz_inversa = []
            return None
        matriz_escalonada = self._matriz.copy()
        matriz_inversa = self.generar_matriz_identidad(len(matriz_escalonada))
        pivote = 0
        while pivote < len(matriz_escalonada) - 1:
            if not self.sin_fila_columna_0(matriz_escalonada):
                self._es_invertible = False
                self._matriz_inversa = []
                return None
            while matriz_escalonada[pivote][pivote] == 0:
                matriz_inversa = self.intercambiar_filas(matriz_inversa, 0)
                matriz_escalonada = self.intercambiar_filas(matriz_escalonada, 0)
            matriz_inversa[pivote] = self.multiplicar_fila_por_escalar(matriz_inversa[pivote],
                                                                       matriz_escalonada[pivote][pivote] ** - 1)
            matriz_escalonada[pivote] = self.multiplicar_fila_por_escalar(matriz_escalonada[pivote],
                                                                          matriz_escalonada[pivote][pivote] ** - 1)
            for i in range(len(matriz_escalonada) - 1 - pivote):
                matriz_inversa[i + 1 + pivote] = self.multiplicar_fila_y_sumarla(matriz_inversa[pivote],
                                                                                 - matriz_escalonada[i + 1 + pivote][
                                                                                       pivote],
                                                                                 matriz_inversa[i + 1 + pivote])
                matriz_escalonada[i + 1 + pivote] = self.multiplicar_fila_y_sumarla(matriz_escalonada[pivote],
                                                                                    - matriz_escalonada[i + 1 + pivote][
                                                                                        pivote],
                                                                                    matriz_escalonada[i + 1 + pivote])
            pivote += 1
        while pivote > 0:
            if not self.sin_fila_columna_0(matriz_escalonada):
                self._es_invertible = False
                self._matriz_inversa = []
                return None
            # while matriz_escalonada[pivote][pivote] == 0:
            #     matriz_escalonada = self.intercambiar_filas(matriz_escalonada, 0, len(matriz_escalonada) - 1)
            matriz_inversa[pivote] = self.multiplicar_fila_por_escalar(matriz_inversa[pivote],
                                                                       matriz_escalonada[pivote][pivote] ** - 1)
            matriz_escalonada[pivote] = self.multiplicar_fila_por_escalar(matriz_escalonada[pivote],
                                                                          matriz_escalonada[pivote][pivote] ** - 1)
            for i in range(pivote):
                matriz_inversa[pivote - i - 1] = self.multiplicar_fila_y_sumarla(matriz_inversa[pivote],
                                                                                 - matriz_escalonada[pivote - i - 1][
                                                                                       pivote],
                                                                                 matriz_inversa[pivote - i - 1])
                matriz_escalonada[pivote - i - 1] = self.multiplicar_fila_y_sumarla(matriz_escalonada[pivote],
                                                                                    - matriz_escalonada[pivote - i - 1][
                                                                                        pivote],
                                                                                    matriz_escalonada[pivote - i - 1])
            pivote -= 1
        self._es_invertible = True
        self._matriz_inversa = matriz_inversa
