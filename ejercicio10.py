def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            return f"no es primo, {n} es divisor"
    return "es primo"


n = int(input("Ingrese un numero: "))
print(f"El numero {n} {es_primo(n)}")
