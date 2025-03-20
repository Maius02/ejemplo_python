"""
Modifique el ejercicio 4 para que dada la lista de número genere dos nuevas
listas, una con los número pares y otras con los que son impares. Imprima
las listas al terminar de procesarlas.
"""
list_impar = []
list_par = []

for i in range(0,10): #3..79
    if( i % 2 != 0 ):
        list_impar.append(i)             #agregar a impar
    else:
        list_par.append(i)              #agregar a par

print(list_impar)
print(list_par)