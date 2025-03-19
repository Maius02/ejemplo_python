"""Haz un programa que pida al usuario que ingrese una temperatura en
grados Celsius y luego convierta esa temperatura a grados Fahrenheit,
mostrando el resultado"""

grados_c = int( input("Ingrese temperatura a convertir (°C):  " ) ) 
grados_f = ( grados_c * 9 ) / 5 + 32
#print ( str(grados_c) + "°C equivalente a " + str(grados_f) + "°F")
print ( f'{grados_c}°C equivalente a {grados_f}°F')