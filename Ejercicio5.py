#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 16:10:20 2021

@author: donald
"""
# EJERCICIO 5
# Calcular la velocidad a la que debe ir un vehículo para recorrer 
# una distancia d en un tiempo t.

distancia = float(input("Ingrese la distancia a recorrer en (Km)"))
tim = float(input("En que tiempo desea llegar (Horas)"))

vel = distancia / tim

print("La velocidad del automovil es ", vel, "(km/hhmm)")