import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

servicio = input("¿Para qué servicio necesitas la contraseña? (por ejemplo: Gmail, Hotmail, etc.): ")

longitud = int(input("Introduce la longitud de tu contraseña: "))

contras = ''.join(random.choice(caracteres) for _ in range(longitud))

print(f"Tu contraseña para {servicio} con longitud {longitud} es: {contras}")

with open("contrasenas.txt", "a") as archivo:
    archivo.write(f"Servicio: {servicio}, Contraseña: {contras} (longitud: {longitud})\n")

print("La contraseña ha sido almacenada en 'contrasenas.txt'")
