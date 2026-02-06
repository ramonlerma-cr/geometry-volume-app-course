# geometry-volume-app-course #

Simulate a simple geometry volume calculator



# Geometry Volume App (Python) #

Calculadora de volúmenes para objetos geométricos 3D (cilindro, caja, cono y esfera).

Incluye pruebas unitarias con `pytest` para validar los cálculos.

## Estructura del proyecto ##

├── geometry/
│ ├── init.py
│ ├── box.py
│ ├── cone.py
│ ├── cylinder.py
│ └── sphere.py
├── tests/
│ ├── init.py
│ ├── test_box.py
│ ├── test_cone.py
│ ├── test_cylinder.py
│ └── test_sphere.py
├── main.py
├── README.md
└── requirements.txt

## Cómo ejecutar el programa ##
Desde la raíz del proyecto, ejecuta:

bash
python main.py

El programa mostrará un menú para seleccionar la figura geométrica
y solicitar las dimensiones necesarias para calcular el volumen.

## Cómo ejecutar las pruebas ##
Desde la raíz del proyecto, ejecuta:

bash
pytest

Si todas las pruebas pasan correctamente, se mostrará un resumen
indicando que todos los tests están en estado passed.

## Requisitos ##
- Python 3.x
- Dependencias del proyecto (instalación):

bash
pip install -r requirements.txt
