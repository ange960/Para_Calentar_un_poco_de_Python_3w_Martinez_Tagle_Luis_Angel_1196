def max_de_tres(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

# Prueba de la función
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
numero3 = float(input("Introduce el tercer número: "))

mayor = max_de_tres(numero1, numero2, numero3)
print(f"El mayor de los tres números es: {mayor}")
