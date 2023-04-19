# PruebaMesa2.py
# 5/4/2023
# Luis Gonzalo Cervantes Rivera
#
# Módulo de prueba para las clases Mesa2, MesaRedonda2 y MesaRectangular2

from MesaRedonda2 import MesaRedonda2
from MesaRectangular2 import MesaRectangular2

mesaRedonda1 = MesaRedonda2('Cubierta Pino', 0.50, 'Pedestal Pino')
mesaRedonda2 = MesaRedonda2('Cubierta Pino', 0.60, 'Pedestal Pino')
mesaRedonda3 = MesaRedonda2('Cubierta Cedro', 0.75, 'Pedestal Cedro')
mesaRectangular1 = MesaRectangular2('Cubierta Pino', 1.0, 1.0, 'Pata Pino')
mesaRectangular2 = MesaRectangular2('Cubierta Pino', 1.0, 1.2, 'Pata Pino')
mesaRectangular3 = MesaRectangular2('Cubierta Cedro', 1.2, 1.5, 'Pata Cedro')

mesas = [mesaRedonda1, mesaRedonda2, mesaRedonda3,
         mesaRectangular1, mesaRectangular2, mesaRectangular3]

print(f'Número de mesas creadas = {MesaRedonda2.contadorMesas()}\n')

for mesa in mesas:
    print(mesa)
    print(f'Área = {mesa.calculaArea():.2f}')
    print(f'Costo = {mesa.calculaCosto():.2f}\n')
