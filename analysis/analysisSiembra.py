import pandas as pd
import matplotlib.pyplot as plt
from data.generators.generadorSiembraArboles import generarDatosSiembraArboles
from helpers.crearTablaHtml import CrearTabla

def construirSiembraDataFrame():
    datosSiembra = generarDatosSiembraArboles()
    siembraDataFrame = pd.DataFrame(datosSiembra,columns=['Corregimiento','HectareasSembradas','Especies Sembradas','Fecha','Nombres','Correos electronicos'])
   #crearTabla(aireDataFrame,"datosaire")
    #Limpiando el dataframe
    #reemplazando valores 
    siembraDataFrame.replace('sin',pd.NA,inplace=True)
    #elimino los registros que no cumplen el criterio
    siembraDataFrame.dropna(inplace=True)
    
    #filtrar DATOS
    #Filtrar es aplicar condiciones logicas
    #que permitan analizar la informacion del DF
    filtroSiembraBueno=siembraDataFrame.query("(HectareasSembradas>=10)and(HectareasSembradas<40)").value_counts()
    filtroSiembraAceptable=siembraDataFrame.query("(HectareasSembradas>=40)and(HectareasSembradas<50)").value_counts()
    filtroSiembraMalo=siembraDataFrame.query("(HectareasSembradas>=50)and(HectareasSembradas<100)").value_counts()

    #ORDENANDO LOS DATOS PARA GRAFICARLOS
    datosOrdenadosSiembra=siembraDataFrame.groupby('Corregimiento')['HectareasSembradas'].mean()
    print(datosOrdenadosSiembra)

    #Grafico la informacion
    plt.figure(figsize=(20,20))
    datosOrdenadosSiembra.plot(kind='bar',color='green')
    plt.title("Indice de contaminacion del aire por comuna en medellin")
    plt.xlabel("Corregimiento")
    plt.ylabel("Hectareas Sembradas")
    plt.grid(True)
    plt.savefig("./imagenes/siembra.png",format='png',dpi=300)
construirSiembraDataFrame()  