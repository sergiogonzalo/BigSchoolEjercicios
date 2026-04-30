import datetime
import pytest
from main import analizar_logs, division_y_limpieza_log, ventana_10_minutos

def test_division_y_limpieza_log():
    log = "[2024-06-01 12:00:00] INFO Inicio del sistema"
    dt, nivel, mensaje = division_y_limpieza_log(log)
    assert dt == "2024-06-01 12:00:00"
    assert nivel == "INFO"
    assert mensaje == "Inicio del sistema"


## Los tests de validar_fecha se eliminan porque la función ya no está activa en main.py

# def test_aumentar_contador_nivel():
#     contador = {"INFO": 0, "ERROR": 0, "WARNING": 0}
#     aumentar_contador_nivel("INFO", contador)
#     assert contador["INFO"] == 1
#     aumentar_contador_nivel("ERROR", contador)
#     assert contador["ERROR"] == 1
#     aumentar_contador_nivel("WARNING", contador)
#     assert contador["WARNING"] == 1

def test_ventana_10_minutos_alerta():
    # Debe imprimir "Alerta Crítica" si hay más de 3 errores en 10 minutos
    timestamps = [
        datetime.datetime(2024, 6, 1, 12, 0, 0),
        datetime.datetime(2024, 6, 1, 12, 1, 0),
        datetime.datetime(2024, 6, 1, 12, 2, 0),
        datetime.datetime(2024, 6, 1, 12, 3, 0),
    ]
    # No assertion, solo comprobamos que no lanza error
    ventana_10_minutos(timestamps)

def test_analizar_logs_varios():
    logs = [
        "[2024-06-01 12:00:00] INFO Inicio del sistema",
        "[2024-06-01 12:01:00] ERROR Error de conexión",
        "[2024-06-01 12:02:00] WARNING Memoria baja",
        "[2024-06-01 12:03:00] ERROR Error de conexión",
        "[2024-06-01 12:04:00] ERROR Error de conexión",
        "[2024-06-01 12:05:00] ERROR Error de conexión"
    ]
    # Solo comprobamos que no lanza error
    analizar_logs(logs)

def test_log_mal_formado():
    log = "[2024-06-01 12:00:00 INFO Inicio del sistema"  # Falta el ']' 
    with pytest.raises(Exception):
        division_y_limpieza_log(log)
