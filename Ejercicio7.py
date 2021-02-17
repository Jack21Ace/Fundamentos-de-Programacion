#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 16:11:31 2021

@author: donald
"""
#Ejercicio 7
#* Realice un programa que simule una calculadora básica, con las operaciones: 
#  suma, resta, multiplicación, división y potencia. 
opt = 0

while True:
    print("""#Operacion a realizar: 
      # 1- Sumar
      # 2- Restar
      # 3- Multiplicar
      # 4- Dividir
      # 5- Potencia
      # 6- Salir""")
       
    opt = int(input("Ingrese una opcion: ")) 

    # PROFE, SU VALIOSA AYUDA CON LOS VALORES VACIOS, 
    #   NULOS O NO DEFINIDOS, ME QUEDO GRANDE ESTE PEDASITO
        
    # if opt == "":
    #   try:
    #       opt = ""
    #   except:    
    #   print"Debe ingresar una opcion para continuar "

#Condicional If else INICIO
    if opt == 0:
        print("0 No es una opcion a elegir ")
    elif opt == 1:
        num1 = int(input("Ingresa primer numero: "))
        num2 = int(input("Ingresa segundo numero: "))
        print("La suma de ", num1, "+", num2, "=", num1+num2)
    elif opt == 2:
        num1 = int(input("Ingresa primer numero: "))
        num2 = int(input("Ingresa segundo numero: "))
        print("La resta de ", num1, "-", num2, "=", num1-num2)
    elif opt == 3:
        num1 = int(input("Ingresa primer numero: "))
        num2 = int(input("Ingresa segundo numero: "))
        print("El resultado de la multiplicación es: ", num1, "*", num2, "=", num1*num2)
    elif opt == 4:
        num1 = int(input("Ingresa primer numero: "))
        num2 = int(input("Ingresa segundo numero: "))
        print("El resultado de la divición es: ", num1, "/", num2, "=", num1/num2)  
    elif opt == 5:
        num1 = int(input("Ingresa primer numero: "))
        num2 = int(input("Ingresa segundo numero: "))
        print("El resultado de la potencia es: ", num1, "", num2, "=", pow(num1,num2)) 
    else:
        print("Hasta luego") 
        break
#Condicional If else FIN