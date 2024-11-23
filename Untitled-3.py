def calcular_longitud(elemento):
    contador = 0
    for _ in elemento:
        contador += 1
    return contador

# Prueba de la función
cadena = input("Introduce una cadena: ")
lista = input("Introduce una lista separada por comas: ").split(',')

longitud_cadena = calcular_longitud(cadena)
longitud_lista = calcular_longitud(lista)

print(f"La longitud de la cadena es: {longitud_cadena}")
print(f"La longitud de la lista es: {longitud_lista}")
