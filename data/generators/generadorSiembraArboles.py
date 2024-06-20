import random

def generarDatosSiembraArboles():
    
    listaDatos = []
    
    
    for _ in range(1000):
        corregimiento = random.choice(['San Antonio de Prado', 'Santa Elena', 'Palmitas San Cristóba', 'Altavista'])
        HectareasSembradas = round(random.uniform(0.5, 10.0), 2)
        especie_sembrada = random.choice(['Roble', 'Eucalipto', 'Pino', 'Cedro', 'Acacia', 'Nogal'])
        fecha = random.choice(['2024-03-01', '2024-03-10', '2024-03-15', '2024-03-22', '2024-03-30','2024-04-05', '2024-05-01', '2024-06-10', '2024-07-20', '2024-08-25','2024-09-05', '2024-10-12']) 
        nombre = random.choice(['Ana Perez', 'Sebastian Jimenez', 'Jose Medina', 'Pedro Cardenas', 'Herminda Gomez', 'Jose Jaramillo', 'Andrea Quintero', 'Doris Remedios', 'Santos Bohorquez'])
        correo = random.choice(['correo@correo.com', 'correo1@correo.com', 'correo2@correo.com', 'correo3@correo.com', 'correo4@correo.com', 'correo5@correo.com'])
        
        
        registro = [corregimiento, HectareasSembradas, especie_sembrada, fecha, nombre, correo]
        
       
        listaDatos.append(registro)
    
    return listaDatos



