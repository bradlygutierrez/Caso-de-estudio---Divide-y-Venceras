"""
Este es el modulo principal del programa

Autor: Bradly Antonio Gutiérrez Córdoba 
ATM Versión 1
11 de Noviembre del 2022 
"""
import funciones as fun


def main():
    fun.agregar_usuarios("050305", "123", "Bradly")
    fun.agregar_usuarios("123", "1234", "Jose")
    fun.imprimir_usuario()
    fun.acceder()


main()
