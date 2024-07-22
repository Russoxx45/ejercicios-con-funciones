def parimpar(n):
    if n % 2 == 0:
        return "par"
    else:
        return "impar"


n = int(input("Ingrese un numero: "))
print(f"El numero {n} es {parimpar(n)}")
