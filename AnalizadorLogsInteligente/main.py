from datetime import datetime, timedelta

def analizar_logs(lista_logs):

    contador_de_niveles = {"INFO": 0, "ERROR": 0, "WARNING": 0}
    mensajes_error = []
    timestamps_error = []

    for log in lista_logs:
   
        datetime_extraido, nivel_extraido, mensaje_extraido = division_y_limpieza_log(log)
        dt_obj = datetime.strptime(datetime_extraido, "%Y-%m-%d %H:%M:%S") #Hace lo mismo que validar_fecha()
        # validar_fecha(dt_obj)
        # aumentar_contador_nivel(nivel_extraido, contador_de_niveles)

        # Corregimos el incremento +=
        if nivel_extraido in contador_de_niveles:
            contador_de_niveles[nivel_extraido] += 1

        if nivel_extraido == "ERROR":
            # datetime_extraido_transformado = datetime.strptime(datetime_extraido, "%Y-%m-%d %H:%M:%S")
            timestamps_error.append(dt_obj)
            mensajes_error.append(mensaje_extraido)

            ventana_10_minutos(timestamps_error)


def division_y_limpieza_log(log: str):

    # [2024-06-01 12:00:00] INFO Inicio del sistema
    datetime_log = log.split("]")[0].strip("[")

    diccionario_partes_log = log.split("] ")[1].split(" ", 1) #Dividimos el split en un diccionario, 1 sola vez
    nivel_log = diccionario_partes_log[0] #Extraemos el nivel del diccionario
    mensaje_extraido = diccionario_partes_log[1] #Extraemos el mensaje del diccionario
    
    return datetime_log, nivel_log, mensaje_extraido

# def validar_fecha(fecha_recibida: datetime):
#     try:
#         datetime.strptime(fecha_recibida, "%Y-%m-%d %H:%M:%S")
#     except ValueError:
#         raise ValueError(f"Fecha no válida: {fecha_recibida}")

# def aumentar_contador_nivel(nivel_recibido: str, contador_de_niveles: dict):

#     match nivel_recibido:

#         case "INFO":
#             contador_de_niveles['INFO'] += 1
#         case "ERROR":
#             contador_de_niveles['ERROR'] += 1
#         case "WARNING":
#             contador_de_niveles['WARNING'] += 1

def ventana_10_minutos(timestamps_error: list):

    # if len(timestamps_error) < 4:
    #     return False


    timestamps_ordenados = sorted(timestamps_error)
    inicio = 0

    for fin in range(len(timestamps_ordenados)):
        while ( timestamps_ordenados[fin] - timestamps_ordenados[inicio]) >= timedelta(minutes=10):
            inicio += 1

        if (fin - inicio + 1) > 3:
            print("Alerta Crítica")

    

if __name__ == "__main__":
    logs = [
        "[2024-06-01 12:00:00] INFO Inicio del sistema",
        "[2024-06-01 12:01:00] ERROR Error de conexión",
        "[2024-06-01 12:02:00] WARNING Memoria baja",
        "[2024-06-01 12:13:00] ERROR Error de conexión",
        "[2024-06-01 12:14:00] ERROR Error de conexión",
        "[2024-06-01 12:15:00] ERROR Error de conexión",
        "[2024-06-01 12:15:01] ERROR Error de conexión"
    ]

    analizar_logs(logs)
