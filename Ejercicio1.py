#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 16:16:15 2021

@author: donald
"""

# EJERCICIO 1
#* Calcular el valor a pagar de una compra realizada, 
# cuyo monto neto es ingresado por el usuario. 
# Considere que el valor del IVA 
#(Impuesto al Valor Agregado - puede variar en cada país), 
#y un descuento del 5% para todas las compras. 
  
 
valorSinIVA=int(input("Ingrese valor a pagar:"))
IVA = valorSinIVA * 19 / 100
total = IVA + valorSinIVA
importe = total * 5 / 100
totalPagar = importe - total

print("El valor : $", total)
print("El valor a pagar es: $", totalPagar)