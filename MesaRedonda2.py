# MesaRedonda2.py
# 5/4/2023
# Luis Gonzalo Cervantes Rivera
#
# Módulo que contiene la clase MesaRedonda2

from Mesa2 import Mesa2
from math import pi


class MesaRedonda2(Mesa2):
    """Clase MesaRedonda2 la cual hereda a la clase abstracta Mesa2
    """

    def __init__(self, cubierta: str, radio: float, pedestal: str):
        """Constructor que inicializa todos los parámetros de la clase

        --------------------------------------------------------------
        Parameters
        ----------
        cubierta: str
            Material de la cubierta de la mesa
        radio: float
            Radio de la mesa
        pedestal: str
            Material del pedestal de la mesa
        """
        super().__init__('Mesa Redonda', cubierta)
        self.__radio = radio
        self.__pedestal = pedestal

    def calculaArea(self):
        """Calcula el área de la mesa

        -----------------------------
        Returns
        -------
        float
            Área de la mesa
        """
        return pi * (self.__radio ** 2)

    def calculaCosto(self):
        """Calcula el costo de la mesa

        ------------------------------
        Returns
        -------
        float
            Costo de la mesa
        """
        return (self.calculaArea() * MesaRedonda2._costos[self._cubierta]) + MesaRedonda2._costos[self.__pedestal]

    def __str__(self):
        """Regresa una cadena con una representación amigable de la clase.

        ------------------------------------------------------------------
        Returns
        -------
        str
            Cadena con una representación amigable de la clase
        """
        return super().__str__() + f', radio: {self.__radio:.2f}, material pedestal: {self.__pedestal}'

    def __repr__(self):
        """Regresa una cadena con una representación no ambigua de la clase.

        --------------------------------------------------------------------
        Returns
        -------
        str
            Cadena con una representación no ambigua de la clase
        """
        return super().__repr__() + f', radio: {self.__radio:.2f}, material pedestal: {self.__pedestal}'


if (__name__ == '__main__'):
    mesaRedonda1 = MesaRedonda2('Cubierta Pino', 0.50, 'Pedestal Pino')
    mesaRedonda2 = MesaRedonda2('Cubierta Pino', 0.60, 'Pedestal Pino')
    mesaRedonda3 = MesaRedonda2('Cubierta Cedro', 0.75, 'Pedestal Cedro')
    mesasRedondas = [mesaRedonda1, mesaRedonda2, mesaRedonda3]

    print(f'Número de mesas creadas = {MesaRedonda2.contadorMesas()}\n')

    for mesa in mesasRedondas:
        print(mesa)
        print(f'Área = {mesa.calculaArea():.2f}')
        print(f'Costo = {mesa.calculaCosto():.2f}\n')
