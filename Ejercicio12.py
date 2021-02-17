#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 17:10:19 2021

@author: donald
"""

#Ejercicio 12
# *  Calcular el sueldo total a recibir de un empleado.  
# El usuario deberá ingresar el número de horas trabajadas 
# y el valor por cada hora. Considere en los cálculos el 
# descuento de seguridad social y una bonificación del 2% 
# para aquellos cuyo sueldo no supere los 300 dólares.         

print("CALCULAR SUELDO")

horasLabor = int(input("Ingrese la cantidad de horas trabajadas: "))
valorHora = int(input("Ingrese el valor de su hora trabajada: "))

neto = horasLabor * valorHora
nomina = neto * 30
descSalud = nomina * 8 / 100
bonif = nomina * 2 / 100
total = nomina - descSalud
"""
print("Valor jornada trabajada", neto)
print("Su nomina mensual es", nomina)
print("Salario con desc de seg social", total)
"""
if nomina <= 1059000:
    print("Su nomina mensual es", nomina)
    print("Estimado trabajador, su pago con descuento a la seguridad social, más pago de bonificaciones es", total+bonif)
else:
    print("Su nomina mensual es", nomina)
    print("Estimado Asalariado, su pago con el descuento a la seguridad social es:", total)