def palindromi(n):
    n = n.lower()
    if n == n[::-1]:
        return f"La palabra {n} es un palíndromo"
    else:
        return f"La palabra {n} no es un palíndromo"


n = input("Ingrese una palabra: ")
print(palindromi(n))
