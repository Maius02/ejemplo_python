"""Desarrolla un programa que solicite al usuario que ingrese su edad y luego
calcule y muestre cuántos años le faltan para alcanzar los 100 años."""

edad = int ( input("Ingrese su edad: ") )

faltante = 100 - edad

if faltante <= 0 : 
    print("Esta muy viejo")
elif faltante > 100 :
    print("Edad invalida")
else :
    print(f'Le falta {faltante} años para cumplir los 100')
