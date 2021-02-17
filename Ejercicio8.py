#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 17:26:13 2021

@author: donald
"""
#Ejercicio 8
# *  Calcular la fuerza que se debe aplicar a un cuerpo para moverlo
# en una mesa horizontal, sabiendo que tiene una masa m (kg) 
# y un coeficiente de rozamiento estático  Us.

pesoObj = int(input("Ingrese el peso del objeto: "))
fuerzaH = int(input("Que fuerza se aplicara: "))
rozamiento = float(input("Ingrese valor para rosamiento estatico: "))

masa = pesoObj * 10
movimiento = rozamiento * masa

if movimiento >= fuerzaH:
    print("La fuerza de rozamiento estatico es de: ", movimiento)
else:
    print("Es un objeto inamovible para para la fuerza aplicada")