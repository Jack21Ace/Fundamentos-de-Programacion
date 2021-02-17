#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 16:09:47 2021

@author: donald
"""
# EJERCICIO 4
#* Realice un programa que obtenga la calificación 
# que debe obtenerse en un examen supletorio, 
# si se conoce que el promedio incluido el supletorio
# para aprobar debe ser mínimo de 3.5 . 
# El usuario debe ingresar las calificaciones 
# en números enteros del primer y segundo bimestre. 

bi1 = int(input("Ingrese sus calificaciones para el Bimestre 1 "))
bi2 = int(input("Ingrese sus calificaciones para el Bimestre 2 "))

prom = (bi1 + bi2) / 2

if prom < 3.5:
    print("Su promedio en las notas es de:", prom)
    print("Debe repetir la carrera")
else:
    print("Felicidades!!!, Pasaste con: ", prom)
    

