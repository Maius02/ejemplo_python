"""Cree un programa que dada una lista de números imprima sólo los que son
pares. Nota: utilice la sentencia continue donde haga falta."""

for i in range(3,80): #3..79
    if( i % 2 != 0 ):
        continue
    print(i)
