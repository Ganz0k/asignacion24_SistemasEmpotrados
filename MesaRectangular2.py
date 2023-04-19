# MesaRectangular.py
# 5/4/2023
# Luis Gonzalo Cervantes Rivera
#
# Módulo que contiene la clase MesaRectangular

from Mesa2 import Mesa2


class MesaRectangular2(Mesa2):
    """Clase MesaRectangular2 la cual hereda a la clase abstracta Mesa2
    """

    def __init__(self, cubierta: str, ancho: float, largo: float, pata: str):
        """Constructor que inicializa todos los parámetros de la clase

        --------------------------------------------------------------
        Parameters
        ----------
        cubierta: str
            Material de la cubierta de la mesa
        ancho: float
            Ancho de la cubierta
        largo: float
            Largo de la cubierta
        pata: str
            Material de las patas de la mesa
        """
        super().__init__('Mesa Rectangular', cubierta)
        self.__ancho = ancho
        self.__largo = largo
        self.__pata = pata

    def calculaArea(self):
        """Calcula el área de la mesa

        -----------------------------
        Returns
        -------
        float
            Área de la mesa
        """
        return self.__ancho * self.__largo

    def calculaCosto(self):
        """Calcula el costo de la mesa

        ------------------------------
        Returns
        -------
        float
            Costo de la mesa
        """
        return (self.calculaArea() * MesaRectangular2._costos[self._cubierta]) + (MesaRectangular2._costos[self.__pata] * 4)

    def __str__(self):
        """Regresa una cadena con una representación amigable de la clase.

        ------------------------------------------------------------------
        Returns
        -------
        str
            Cadena con una representación amigable de la clase
        """
        return super().__str__() + f', ancho: {self.__ancho:.2f}, largo: {self.__largo:.2f}, material pata: {self.__pata}'

    def __repr__(self):
        """Regresa una cadena con una representación no ambigua de la clase.

        --------------------------------------------------------------------
        Returns
        -------
        str
            Cadena con una representación no ambigua de la clase
        """
        return super().__repr__() + f', ancho: {self.__ancho:.2f}, largo: {self.__largo:.2f}, material pata: {self.__costoPata}'


if (__name__ == '__main__'):
    mesaRectangular1 = MesaRectangular2('Cubierta Pino', 1.0, 1.0, 'Pata Pino')
    mesaRectangular2 = MesaRectangular2('Cubierta Pino', 1.0, 1.2, 'Pata Pino')
    mesaRectangular3 = MesaRectangular2(
        'Cubierta Cedro', 1.2, 1.5, 'Pata Cedro')
    mesasRectangulares = [mesaRectangular1, mesaRectangular2, mesaRectangular3]

    print(f'Número de mesas creadas = {MesaRectangular2.contadorMesas()}\n')

    for mesa in mesasRectangulares:
        print(mesa)
        print(f'Área = {mesa.calculaArea():.2f}')
        print(f'Costo = {mesa.calculaCosto():.2f}\n')
