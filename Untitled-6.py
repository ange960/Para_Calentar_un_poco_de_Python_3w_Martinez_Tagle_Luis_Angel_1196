def inversa(cadena):
    """
    Invierte el orden de los caracteres en una cadena.

    Args:
    cadena (str): La cadena que se desea invertir.

    Returns:
    str: La cadena invertida.
    """
    invertida = ""
    for caracter in cadena:
        invertida = caracter + invertida
    return invertida

# Prueba de la función
texto = input("Introduce una cadena para invertir: ")

resultado = inversa(texto)
print(f"La cadena invertida es: '{resultado}'")
