"""
En este módulo se encuntran las clases que se usaran en el programa

Autor: Bradly Antonio Gutiérrez Córdoba 
ATM Versión 1
11 de Noviembre del 2022 
"""


class Cuenta:
    def __init__(self, num, pin, name):
        self.NumeroDeTarjeta = num
        self.Pin = pin
        self.Saldo = 0
        self.Nombre = name

    def __str__(self):
        return f"""
Nombre: {self.Nombre}
Numero de tarjeta: {self.NumeroDeTarjeta}
Pin: {self.Pin}
Saldo: {self.Saldo}        
"""
