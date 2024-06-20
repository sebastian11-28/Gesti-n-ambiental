import random

def generarDatosCalidadAire():
    
    listaDatos = []
    for i in range(1000):
        nombre=random.choice(['ana perez','sebastian bohorquez','sebastian jimenez','jose medina','pedro cardenas','herminda gomez','jose jaramillo','andrea quintero','doris remedios','santos bohorquez'])
        comuna = random.randint(1,14)
        ica= random.randint(10,80)
        fecha=random.choice(['2024-04-18','2024-04-24','2024-05-14','2024-05-13'])
        correo =random.choice(['correo@correo.com','correo1@correo.com','correo2@correo.com','correo3@correo.com','correo4@correo.com','correo5@correo.com'])
        
        encuesta=[nombre,comuna,ica,fecha,correo]
        
        listaDatos.append(encuesta)
        
    return listaDatos

