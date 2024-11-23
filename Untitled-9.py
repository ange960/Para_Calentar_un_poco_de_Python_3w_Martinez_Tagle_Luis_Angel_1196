def generar_n_caracteres(n, caracter):
    # Devolver el caracter repetido n veces
    return caracter * n

# Ejemplo de uso
print(generar_n_caracteres(5, "x"))  # Debería devolver "xxxxx"
print(generar_n_caracteres(3, "*"))  # Debería devolver "***"
print(generar_n_caracteres(7, "-"))  # Debería devolver "-------"
