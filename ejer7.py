"""
Escribe un programa que tome una lista de números enteros como entrada
del usuario. Luego, convierte cada número en la lista a string y únelos en
una sola cadena, separados por guiones ('-'). Sin embargo, excluye cualquier
número que sea múltiplo de 3 de la cadena final.
"""
list_nros = []
cadena = ""

#ingreso lista de numeros enteros
for _ in range(10):
    nro = int ( input("ingrese un nro entero: ") )
    list_nros.append(nro)

print(f'Lista de numeros enteros ingresada {list_nros}')

#convierto cada nro en la lista a string y concateno en la var cadena
for nro in list_nros:
    if nro % 3 == 0:
        continue
    cadena = cadena + str(nro) + " - "

print(f'Cadena {cadena}')