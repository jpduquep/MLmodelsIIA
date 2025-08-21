'''

Ejercicio 01 -

En python hacer un EDA con un conjunto de datos simulado o conjunto de datos sintetico de tal manera que pueda hacer visualizacion
de datos, analisis exploratorio, mostrar graficas de tendencia, de barras, dispersion, graficos de pastel histogramas.
Emplear Streamlit para hacer una visualizacion dinamica, para usar botones desplazables, que permitan generar un conjunto de datos y yo elija
las muestras hasta 500 y hasta 6 columnas, que icnluya variables cuantitativas, cualitativas o mixtas sobre deportes.

El usuario podra elegir las columnas, las graficas, mostrar la tabla e interactuar con la plataforma

Proporcionar las librerias en un requirements.txt y el codigo para la app.py que sera desplegada en Streamlit

'''

#Conjunto de datos simulado sintetico para visualizacion de datos
import pandas as pd
import random

cols = ["id", "nombre_equipo", "partidos_ganados", "partidos_empatados", "partidos_perdidos", "puntos"]

data = []
for i in range(1, 501):
    data.append({
        "id": i,
        "nombre_equipo": f"Equipo {i}",
        "partidos_ganados": random.randint(0, 30),
        "partidos_empatados": random.randint(0, 30),
        "partidos_perdidos": random.randint(0, 30),
        "puntos": random.randint(0, 90)
    })


df = pd.DataFrame(data, columns=cols)


print("Títulos columnas:", df.columns.tolist())
print(df.head())

# Análisis exploratorio de ese conjunto
def analisis_exploratorio(grafo):
    pass


#Mostrar graficas: Tendencia, Barras, Dispersión, Pastel, Histogramas


#Configuracion con Streamlit para visualizacion dinamica con botones desplazables, que permita generar conjuntos de datos
#se pueda elegir las muestras hasta 500 y hasta 6 columnas, que incluya variables cuantitativas, cualitativas o mixtas sobre deportes.