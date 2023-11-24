def convertirAFahrenheit(temperatura):
    return temperatura * 9 / 5 + 32

def obtenerTemperaturasMaximas(datos_dia):
    return datos_dia["maxima"]

# Lista original de temperaturas en grados Celsius
listaTemperaturas = [
    {"fecha": "2023-11-21", "maxima": 25},
    {"fecha": "2023-11-22", "maxima": 20},
    {"fecha": "2023-11-23", "maxima": 27}
]

# Utilizando map para convertir las temperaturas de Celsius a Fahrenheit
listaTemperaturasFahrenheit = list(map(lambda x: convertirAFahrenheit(x["maxima"]), listaTemperaturas))

# Utilizando filter para obtener las temperaturas máximas del día
listaTemperaturasMax = list(map(obtenerTemperaturasMaximas, listaTemperaturas))

print("Temperaturas en Fahrenheit:", listaTemperaturasFahrenheit)
print("Temperaturas máximas del día:", listaTemperaturasMax)
