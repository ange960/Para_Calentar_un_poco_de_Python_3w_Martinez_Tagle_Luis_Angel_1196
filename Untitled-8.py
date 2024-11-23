def superposicion(lista1, lista2):
    # Recorremos cada elemento de la primera lista
    for elemento1 in lista1:
        # Recorremos cada elemento de la segunda lista
        for elemento2 in lista2:
            # Si encontramos un elemento común, devolvemos True
            if elemento1 == elemento2:
                return True
    # Si no encontramos ningún elemento común, devolvemos False
    return False

# Ejemplo de uso
print(superposicion([1, 2, 3], [3, 4, 5]))  # Debería devolver True
print(superposicion([1, 2, 3], [4, 5, 6]))  # Debería devolver False
