# DSS
[![Build Status](https://travis-ci.org/olmo/DSS.svg?branch=master)](https://travis-ci.org/olmo/DSS)

Implementación en python de firmas mediante DSS.
La interfaz gráfica funciona mediante WXPython, por lo que es necesario tener instalado el paquete:
http://www.wxpython.org/download.php

El archivo a ejecutar es dds.pyw

Para realizar la aplicación se ha utilizado la plantilla disponible en https://github.com/olmo/plantilla-git
Para utilizarla se hace un clone de la plantilla, y luego un clone del repositorio de la siguiente forma:

git clone https://github.com/olmo/DSS --template plantilla-git

La plantilla tiene activado un hook por defecto (pre-commit) que no permite realizar un commit que contenga archivos .pyc, además de comprobar la sintaxis de los archivos python usando pylint.