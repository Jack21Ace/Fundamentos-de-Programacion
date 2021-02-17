#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 16:13:28 2021

@author: donald
"""
    
#Ejercicio 9
# * Leer la temperatura en grados Celsius y convertirla a grados Kelvin 
# y a grados Farenheit 

C = int(input("Ingrese la temperatura en grados Celsius: "))

K = C + 273.15
F = (C*1.8) + 32

print("El resultado en Kelvin es: " , K)
print("El resultado en Farenheit es: " , F)
