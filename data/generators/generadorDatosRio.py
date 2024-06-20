import random

def generarDatosContaminacionRio():
    
    listaDatos = []
     
    
    
    
    
    for _ in range(1000):
        empresa = random.choice(['Empresa A', 'Empresa B', 'Empresa C', 'Empresa D', 'Empresa E'])
        comuna = random.randint(1,14)
        dqo = round(random.uniform(10, 500), 2)  # DQO en mg/L
        fecha = random.choice(['2024-03-01', '2024-03-10', '2024-03-15', '2024-03-22', '2024-03-30','2024-04-05', '2024-05-01', '2024-06-10', '2024-07-20', '2024-08-25','2024-09-05', '2024-10-12' ]) 
        correo = random.choice(['correo@correo.com', 'correo1@correo.com', 'correo2@correo.com', 'correo3@correo.com', 'correo4@correo.com', 'correo5@correo.com'])
        
        
        registro = [dqo, empresa, comuna, fecha, correo]
        
        
        listaDatos.append(registro)
    
    return listaDatos


