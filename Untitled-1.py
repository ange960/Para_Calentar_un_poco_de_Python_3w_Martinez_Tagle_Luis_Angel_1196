def max(a, b):
    if a > b:
        return a
    else:
        return b

# Prueba de la función
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

mayor = max(numero1, numero2)
print(f"El mayor de los dos números es: {mayor}")
