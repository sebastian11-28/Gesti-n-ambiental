import pandas as pd
import matplotlib.pyplot as plt
from data.generators.generadorRuido import generarDatosRuidoAmbiental
from helpers.crearTablaHtml import CrearTabla


def construirRuidoDataFrame():
    # Generar datos de ruido ambiental
    datosRuido = generarDatosRuidoAmbiental()
    
    # Crear DataFrame
    ruidoDataFrame = pd.DataFrame(datosRuido, columns=['Nombre', 'Comuna', 'decibelios Diurnos', 'decibelios Nocturnos', 'Fecha', 'Correo'])
    
    # Filtrar y limpiar datos
    ruidoDataFrame.replace('sin', pd.NA, inplace=True)
    ruidoDataFrame.dropna(inplace=True)
    
    # Filtrar y contar según criterios de decibelios nocturnos
    filtroRuidoBueno = ruidoDataFrame.query("`decibelios Nocturnos` >= 45 and `decibelios Nocturnos` < 55").shape[0]
    filtroRuidoAceptable = ruidoDataFrame.query("`decibelios Nocturnos` >= 55 and `decibelios Nocturnos` < 65").shape[0]
    filtroRuidoMalo = ruidoDataFrame.query("`decibelios Nocturnos` >= 65 and `decibelios Nocturnos` < 80").shape[0]
    
    print("Ruido Bueno:", filtroRuidoBueno)
    print("Ruido Aceptable:", filtroRuidoAceptable)
    print("Ruido Malo:", filtroRuidoMalo)
    
    # Calcular promedio de decibelios nocturnos por comuna
    datosOrdenadosRuido = ruidoDataFrame.groupby('Comuna')['decibelios Nocturnos'].mean()
    
    # Verificar si hay datos para graficar
    if datosOrdenadosRuido.empty:
        print("No hay datos disponibles para graficar.")
        return
    
    print("Promedio de decibelios nocturnos por comuna:\n", datosOrdenadosRuido)
    
    # Graficar la información
    plt.figure(figsize=(10, 6))
    datosOrdenadosRuido.plot(kind='bar', color='blue')
    plt.title("Índice de contaminación del ruido por comuna en Medellín")
    plt.xlabel("Comuna")
    plt.ylabel("Decibelios Nocturnos (Promedio)")
    plt.grid(True)
    plt.savefig("./imagenes/ruido.png", format='png', dpi=300)
    plt.show()

construirRuidoDataFrame()
