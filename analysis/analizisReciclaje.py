import pandas as pd
import matplotlib.pyplot as plt

from data.generators.generadorReciclaje import generarDatosReciclajeUrbano
from helpers.crearTablaHtml import CrearTabla


def construirReciclajeDataFrame():
    datosReciclaje = generarDatosReciclajeUrbano()
    reciclajeDataFrame = pd.DataFrame(datosReciclaje, columns=['Nombre', 'Comuna', 'Tipo residuo', 'Frecuencia', 'Fecha'])

    reciclajeDataFrame.replace('sin', pd.NA, inplace=True)
    # Elimino los registros que no cumplen el criterio
    reciclajeDataFrame.dropna(inplace=True)
    
    # Filtrar DATOS
    # Filtrar es aplicar condiciones lógicas
    # que permitan analizar la información del DF
    filtroReciclajeBueno = reciclajeDataFrame.query("Frecuencia == 'Diario'").value_counts()
    filtroReciclajeAceptable = reciclajeDataFrame.query("Frecuencia == 'Semanal' or Frecuencia == 'Quincenal'").value_counts()
    filtroReciclajeMalo = reciclajeDataFrame.query("Frecuencia == 'Mensual'").value_counts()

    # Mostrando los resultados de los filtros
    print("Reciclaje Bueno:\n", filtroReciclajeBueno)
    print("Reciclaje Aceptable:\n", filtroReciclajeAceptable)
    print("Reciclaje Malo:\n", filtroReciclajeMalo)

    # Ordenando los datos para graficar
    datosOrdenadosReciclaje = reciclajeDataFrame.groupby('Comuna').size()
    print(datosOrdenadosReciclaje)

    # Graficar la información
    plt.figure(figsize=(10, 6))
    datosOrdenadosReciclaje.plot(kind='bar', color='orange')
    plt.title("Índice de reciclaje por comuna en Medellín")
    plt.xlabel("Comuna")
    plt.ylabel("Frecuencia")
    plt.grid(True)
    plt.savefig("./imagenes/reciclaje.png", format='png', dpi=300)
    
construirReciclajeDataFrame()
