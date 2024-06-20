import pandas as pd
import matplotlib.pyplot as plt
from data.generators.generadorDatosRio import generarDatosContaminacionRio
from helpers.crearTablaHtml import CrearTabla

def construirContaminacioRioDataFrame():
    datosContaminacionRio = generarDatosContaminacionRio()
    contaminacionRioDataFrame = pd.DataFrame(datosContaminacionRio,columns=['dqo', 'empresa', 'comuna', 'fecha', 'correo'])
    #CrearTabla(contaminacionRioDataFrame,"ContaminacionRio")
    #print(contaminacionRioDataFrame)
    
      #reemplazando valores 
    contaminacionRioDataFrame.replace('sin',pd.NA,inplace=True)
    #elimino los registros que no cumplen el criterio
    contaminacionRioDataFrame.dropna(inplace=True)
    
    #filtrar DATOS
    #Filtrar es aplicar condiciones logicas
    #que permitan analizar la informacion del DF
    filtroContaminacionRioBueno=contaminacionRioDataFrame.query("(dqo>=10)and(dqo<40)").value_counts()
    filtroContaminacionRioAceptable=contaminacionRioDataFrame.query("(dqo>=40)and(dqo<50)").value_counts()
    filtroContaminacionRioeMalo=contaminacionRioDataFrame.query("(dqo>=50)and(dqo<100)").value_counts()

    #ORDENANDO LOS DATOS PARA GRAFICARLOS
    datosOrdenadosContaminacionRio=contaminacionRioDataFrame.groupby('comuna')['dqo'].mean()
    print(datosContaminacionRio)

    #Grafico la informacion
    plt.figure(figsize=(20,20))
    datosOrdenadosContaminacionRio.plot(kind='bar',color='red')
    plt.title("Indice de contaminacion del rio por comuna en medellin")
    plt.xlabel("Comuna")
    plt.ylabel("dqo")
    plt.grid(True)
    plt.savefig("./imagenes/contaminacionRio.png",format='png',dpi=300)
    
construirContaminacioRioDataFrame()    
