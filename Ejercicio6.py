#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 16:10:58 2021

@author: donald
"""
# EJERCICIO 6
#* Realice un programa que resuelva lo siguiente: Si n Empleados 
# realizan una actividad en k horas, ¿cuántos empleados se necesitarán 
# para realizar la misma actividad en k1 horas? 

cant_emple = int(input("Empleados en producción: "))
horas = int(input("Cantidad de horas en produccion: "))

RQ = cant_emple*horas
requerimiento = RQ - cant_emple

if requerimiento >= 1:
    print("se necesita: ", requerimiento, " para realizar la actividad en una hora")
else:
    print("no es necesario mas personal")