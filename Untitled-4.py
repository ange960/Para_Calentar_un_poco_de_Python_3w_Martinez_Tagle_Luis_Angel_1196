def es_vocal(caracter):
    """
    Verifica si el carácter proporcionado es una vocal.
    
    Args:
    caracter (str): Un único carácter que se desea verificar.

    Returns:
    bool: True si el carácter es una vocal, False en caso contrario.
    """
    # Definir las vocales (minúsculas y mayúsculas)
    vocales = 'aeiouAEIOU'
    
    # Validar que se introduzca exactamente un carácter
    if len(caracter) != 1:
        print("Por favor, introduce un único carácter.")
        return False
    
    # Comprobar si el carácter está en la lista de vocales
    if caracter in vocales:
        return True
    else:
        return False

# Prueba de la función
print("Bienvenido al verificador de vocales.")
print("Por favor, introduce un carácter para comprobar si es una vocal.")
caracter = input("Introduce un carácter: ")

resultado = es_vocal(caracter)

if resultado:
    print(f"¡Correcto! El carácter '{caracter}' es una vocal.")
else:
    if len(caracter) != 1:
        print("Error: No se introdujo un único carácter.")
    else:
        print(f"El carácter '{caracter}' no es una vocal.")
