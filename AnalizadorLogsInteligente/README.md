Reto Nivel 1: El Analizador de Logs Inteligente

Para calentar motores y ver cómo estás estructurando la lógica de datos sin librerías pesadas (como Pandas), vamos a empezar con un problema de procesamiento de strings y gestión de estados.

El Enunciado
Imagina que recibes un flujo de logs de un servidor en formato de texto plano. Cada línea tiene el siguiente formato:
[TIMESTAMP] LEVEL: MESSAGE

Ejemplo:
[2026-04-29 14:30:01] INFO: User logged in
[2026-04-29 14:31:05] ERROR: Database connection failed

Tu tarea es escribir una función o clase que:

Reciba una lista de estas cadenas de texto.

Contabilice cuántos mensajes hay por cada nivel (INFO, ERROR, WARNING).

Extraiga todos los mensajes de error en una lista independiente.

Detección de Anomalías: Si aparecen más de 3 errores en una ventana de menos de 10 minutos, debe imprimir un mensaje de "Alerta Crítica".

Restricciones
No puedes usar Pandas ni Polars.

Usa el módulo datetime para gestionar los tiempos.

Tu código debe ser robusto ante líneas mal formateadas (debe ignorarlas sin romper el programa).