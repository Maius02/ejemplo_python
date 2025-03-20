import string

print("Generador de claves!")

chars = string.ascii_letters + string.digits + string.puntuation

password = ""

length = 10

for _ in range(length):
    password = password + random.choise(chars)

print ("Contraseña generada: ", password)
