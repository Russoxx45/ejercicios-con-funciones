def vocalcounter(t):
    vowels = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú']
    count = 0
    for i in t:
        if i in vowels:
            count += 1
    return count


t = input("Ingrese una frase o palabra: ").lower()
print(f"La frase o palabra ingresa tiene {vocalcounter(t)} vocales")
