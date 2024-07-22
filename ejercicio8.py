def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact


n = int(input("Ingrese un numero: "))
print("El factorial de", n, "es", factorial(n))
