import random

def generarDatosReciclajeUrbano():
    listaDatos = []

    for _ in range(1000):
        nombre = random.choice(['Ana Perez', 'Sebastian Jimenez', 'Jose Medina', 'Pedro Cardenas', 'Herminda Gomez', 'Jose Jaramillo', 'Andrea Quintero', 'Doris Remedios', 'Santos Bohorquez'])
        comuna = random.randint(1, 14)
        tipo_residuo = random.choice(['Plástico', 'Vidrio', 'Papel', 'Orgánico', 'Metálico'])
        frecuencia = random.choice(['Diario', 'Semanal', 'Quincenal', 'Mensual'])
        fecha = random.choice(['2024-04-18', '2024-04-24', '2024-05-14', '2024-05-13'])

        registro = [comuna, tipo_residuo, frecuencia, fecha, nombre]
        listaDatos.append(registro)

    return listaDatos
