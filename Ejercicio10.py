#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 16:15:31 2021

@author: donald
"""

#Ejercicio 10
# *  Calcular el área y perímetro de un rectángulo.

base = int(input("Ingrese la BASE para el triangulo: "))
altura = int(input("Ingrese la ALTURA: "))

area = base*altura
perimetro = (base + altura)*2

print("El area del rectangulo es: ", area)
print("El perimetro del rectangulo es: ", perimetro)