def farenheit(celcius):
    farenheit = (celcius * 1.8)-32
    return farenheit


celcius = float(input("Ingrese la temperatura en celcius(°C): "))
print(farenheit(celcius), "°F")
