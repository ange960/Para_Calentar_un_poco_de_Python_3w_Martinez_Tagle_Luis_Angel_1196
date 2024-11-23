def sum(lista):
    """
    Suma todos los números de una lista.
    
    Args:
    lista (list): Lista de números.

    Returns:
    int/float: La suma de los números de la lista.
    """
    resultado = 0
    for num in lista:
        resultado += num
    return resultado

def multip(lista):
    """
    Multiplica todos los números de una lista.
    
    Args:
    lista (list): Lista de números.

    Returns:
    int/float: El producto de los números de la lista.
    """
    resultado = 1
    for num in lista:
        resultado *= num
    return resultado

# Prueba de las funciones
numeros = [1, 2, 3, 4]

suma = sum(numeros)
producto = multip(numeros)

print(f"La suma de {numeros} es: {suma}")
print(f"El producto de {numeros} es: {producto}")
