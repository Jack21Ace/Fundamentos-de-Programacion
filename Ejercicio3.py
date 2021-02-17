#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 16:08:16 2021

@author: donald
"""
# EJERCICIO 3
#*  Realice un programa que obtenga el índice de masa 
#corporal de una persona, ingresando la estatura 
#en centímetros y el peso en kilos. 
 
peso = float(input("Escriba su peso en (Kg): "))
estatura = float(input("Escriba estatura en (m): "))

IMC = peso / (estatura **2)

print("Su IMC es:", IMC)

if IMC < 18.5:
    print("Ud se encuentra en bajo peso")
elif IMC > 18.4 and IMC <= 24.9:
    print("Su peso es Normal")
elif IMC > 25 and IMC <= 29.9:
    print("Ud tiene sobre peso")
else:
    print("Ud tiene Obesidad")
    
