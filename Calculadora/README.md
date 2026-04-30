
# Calculadora en Python

## Descripción
Este proyecto implementa una calculadora básica en Python, capaz de realizar operaciones de suma, resta, multiplicación y división, con manejo de errores como la división por cero. Incluye una interfaz de línea de comandos y pruebas unitarias con `pytest` para validar su funcionamiento.

## Estructura del proyecto
- `calculadora.py`: Implementación de la clase `Calculator` con las operaciones matemáticas.
- `main.py`: Interfaz de línea de comandos para interactuar con la calculadora.
- `test_calculadora.py`: Pruebas unitarias usando `pytest`.
- `README.md`: Documentación del proyecto.

## Instalación
1. Clona este repositorio o descarga los archivos.
2. Asegúrate de tener Python 3 instalado.
3. (Opcional, pero recomendado) Instala las dependencias de desarrollo:

```bash
pip install pytest
```

## Uso
Ejecuta el archivo principal desde la terminal:

```bash
python main.py
```

Sigue las instrucciones para ingresar los números y seleccionar la operación.

## Pruebas
Para ejecutar las pruebas unitarias con `pytest`:

```bash
pytest test_calculadora.py
```

También puedes usar `unittest` si lo prefieres:

```bash
python -m unittest test_calculadora.py
```

---

# Calculadora en Python (Español)

## Descripción
Este proyecto implementa una calculadora básica en Python, capaz de realizar operaciones de suma, resta, multiplicación y división, con manejo de errores como la división por cero. Incluye pruebas unitarias para validar su funcionamiento.

## Instalación
1. Descarga o clona el repositorio.
2. Verifica que tienes Python 3 instalado.

## Uso
Ejecuta en la terminal:

```bash
python calculadora.py
```
Ingresa los números solicitados y obtendrás los resultados de las operaciones.

## Pruebas
Para correr los tests:

```bash
python -m unittest test_calculadora.py
```
