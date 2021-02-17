#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 16:07:32 2021

@author: donald
"""
# EJERCICIO 2
#*  Calcular el área de un círculo y longitud de su circunferencia. 

import math

radio=float(input("Ingrese el radio para el circulo "))
area = math.pi*pow(radio,2)
longitud = 2 * math.pi * radio 
circun = (radio * radio) / 2


print("El Area del circulo es: ", area)
print("La longitud del circulo es: ", longitud)
print("La circunferencia es del circulo es: ", circun)
