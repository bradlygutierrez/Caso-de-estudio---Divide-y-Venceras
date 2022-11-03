"""
En este módulo se encuntran las funciones del programa programa

Autor: Bradly Antonio Gutiérrez Córdoba 
ATM Versión 1
11 de Noviembre del 2022 
"""
from clases import Cuenta
import os
import time

Cuentas = []


def acceder():
    estilizar("Color 0A")
    numero = input("Numero de tarjeta: ")
    pin = input("Pin: ")

    if (verificar_identidad(numero, pin) == True):
        op = 0
        while (op != 4):
            time.sleep(0.2)
            menu()
            op = int(input("Elija su opción: "))
            if (op == 1):
                depositar(numero)
            elif (op == 2):
                retirar(numero)
            elif (op == 3):
                verSaldos(numero)
            elif (op == 4):
                print("Saliendo...")
                time.sleep(0.5)
                break
    else:
        print("El usario no existe o los credenciales son incorrectos")
        time.sleep(0.6)
        acceder()


def menu():
    print("Bienvenido ")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Ver saldos")
    print("4. Salir")


def verSaldos(num):
    estilizar("Color 0B")
    user = buscar_usuario(num)
    print("=" * 50)
    print("Nombre de usuario: ", user.Nombre)
    print("User con nùmero de tarjeta: ", user.NumeroDeTarjeta)
    print("Su saldo es de: ", user.Saldo)
    print("=" * 50)
    return


def buscar_usuario(num):
    for cuenta in Cuentas:
        if (cuenta.NumeroDeTarjeta == num):
            return cuenta
    else:
        return False


def verificar_identidad(numTar, pin):
    cuenta = buscar_usuario(numTar)
    if (cuenta != False):
        if (cuenta.NumeroDeTarjeta == numTar and pin == cuenta.Pin):
            return True
    else:
        return False


def agregar_usuarios(num, pin, nom):
    newUser = Cuenta(num, pin, nom)
    Cuentas.append(newUser)


def depositar(num):
    estilizar("Color 0C")
    saldo = pedir_monto()
    user = buscar_usuario(num)
    if saldo % 100 == 0:
        user.Saldo += saldo
    else:
        print("El valor debe de ser multiplo de 100")


def retirar(num):
    estilizar("Color 0D")
    monto = pedir_monto()
    user = buscar_usuario(num)
    if monto % 100 == 0:
        if (user.Saldo >= monto):
            user.Saldo -= monto
        else:
            print("No posee el saldo sufieciente")
    else:
        print("El valor debe de ser multiplo de 100")
    return 0


def imprimir_usuario():
    for i in Cuentas:
        print("="*50)
        print(i)
        print("="*50)


def estilizar(color):
    a = color
    print("Cargando...")
    os.system("cls")
    time.sleep(0.4)
    os.system(a)


def pedir_monto():
    print("=" * 50)
    monto = int(input("Ingrese el monto: "))
    print("=" * 50)
    return monto
