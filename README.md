# SurveyGeneratorBot
Este script Python está diseñado para automatizar el proceso de llenado de encuestas en un sitio web específico utilizando Selenium, una biblioteca de automatización de navegadores web. El script simula la interacción humana con el navegador Firefox para completar una serie de formularios en línea.

El flujo de trabajo del script implica:

- Configuración del navegador Firefox con Selenium.
- Navegación a una URL particular que corresponde a una encuesta en línea.
- Llenado secuencial de múltiples páginas de la encuesta, seleccionando opciones y proporcionando comentarios aleatorios según parámetros predefinidos.
- Finalización y envío de la encuesta.

El script utiliza funciones JavaScript incrustadas para interactuar con elementos específicos de la página web, como botones y campos de entrada, permitiendo la selección de opciones y la introducción de texto de manera dinámica.

Para ejecutar este script con éxito, se requiere la instalación previa de Python, la biblioteca Selenium y el controlador de Selenium para Firefox (geckodriver), así como una conexión a Internet para acceder al sitio web de la encuesta.

Este script proporciona una solución automatizada para la tarea repetitiva y laboriosa de completar encuestas en línea, lo que ahorra tiempo y esfuerzo para el usuario.

# Requisitos
1.- Python instalado: Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde el sitio web oficial de Python e instalarlo siguiendo las instrucciones.

2.- Instalar Selenium: Este script utiliza Selenium, por lo que necesitarás instalarlo. Puedes instalarlo utilizando pip, el gestor de paquetes de Python. Ejecuta el siguiente comando en tu terminal o símbolo del sistema:
~~~
pip install selenium
~~~
Descargar e instalar el controlador de Selenium para Firefox (geckodriver) inlcuido en este repositorio: Selenium requiere un controlador específico para el navegador que estás utilizando. En este caso, el script está configurado para Firefox, así que necesitarás descargar geckodriver. Puedes descargarlo desde el sitio web oficial de Selenium WebDriver: https://github.com/mozilla/geckodriver/releases y luego agregar la ubicación del archivo ejecutable a tu variable de entorno PATH o especificar su ubicación directamente en el script.

Actualizar las rutas de los controladores si es necesario: Si has descargado geckodriver y lo has colocado en una ubicación diferente a la proporcionada en el script (`'/path/to/geckodriver'`), asegúrate de actualizar esa ruta en el script con la ubicación correcta.

# Ejecucion
Abre una terminal o símbolo del sistema en el directorio donde guardaste el archivo ".py".

Ejecuta el script Python utilizando el intérprete de Python. Puedes hacerlo escribiendo el siguiente comando en la terminal:
~~~
python encuesta.py
~~~
El script comenzará a ejecutarse y automatizará el proceso de llenado de formularios en el sitio web especificado. Este script realiza 5 encuestas por cada ejecucion.

### Desarrollador:
- [Carlos Daniel Angel Padilla (DarkCobra7423)](https://github.com/DarkCobra7423)
