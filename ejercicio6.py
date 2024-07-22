def max(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3


n1 = float(input("Ingrese el numero 1: "))
n2 = float(input("Ingrese el numero 2: "))
n3 = float(input("Ingrese el numero 3: "))

print("El máximo de los tres números es:", max(n1, n2, n3))
