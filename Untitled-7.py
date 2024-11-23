def es_palindromo(palabra):
    # Convertir la palabra a minúsculas y eliminar espacios (si lo deseas)
    palabra = palabra.lower().replace(" ", "")
    
    # Comprobar si la palabra es igual a su inversa
    return palabra == palabra[::-1]

# Ejemplo de uso
print(es_palindromo("radar de mis carnales los ,mas perrones hasta la muerte "))  # Debería devolver True
print(es_palindromo("valenhtin,piedra,jose gutierrez y yo el mas guapo "))   # Debería devolver False
