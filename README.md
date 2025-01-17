# Proyecto de Pruebas Automatizadas con Selenium y unittest

## Descripción
Este proyecto contiene pruebas automatizadas para la aplicación web usando Selenium y unittest en Python. Las pruebas verifican la funcionalidad de registro, incluyendo la validación de campos, la verificación de mensajes de error y la habilitación del botón de envío cuando todos los campos son válidos. Además, el proyecto genera informes detallados en formato XML y captura capturas de pantalla en caso de errores.

## Estructura del Proyecto
```plaintext
mi_proyecto_automatizacion/
│
├── drivers/
│   ├── __init__.py
│   └── chrome_driver.py
│
├── pages/
│   ├── __init__.py
│   └── login_page.py
│
├── tests/
│   ├── __init__.py
│   └── test_login.py
│
├── utils/
│   ├── __init__.py
│   └── constantes.py
│
├── test-reports/
│   └── (Informes XML generados durante las pruebas)
│
├── requirements.txt
└── README.md



## Instalacion
git clone https://github.com/usuario/mi_proyecto_automatizacion.git
cd mi_proyecto_automatizacion

## Ejecucion de prueba
# navega hasta la raiz del proyecto
cd C:ProyectosSofware\SeleniumPython

## ejecuta el siguiente script desde la terminal
# python -m unittest discover -s tests -p "test_*.py"


Generación de Informes
Los informes se generan automáticamente en el directorio test-reports en formato XML.
 Para visualizar los informes, puedes abrir los archivos XML en cualquier editor de texto
  o herramienta compatible con XML.

Instalación de Dependencias
Puedes instalar todas las dependencias listadas en requirements.txt con el siguiente comando:

#  pip install -r requirements.txt
