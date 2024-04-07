# Explicacion de como se realizo el proyecto y su Ejecucion
## Instalación de PostgreSQL desde Binarios
Para ejecutar este proyecto, se requiere PostgreSQL. La versión necesaria es la 14.11, que se puede descargar desde el siguiente enlace: [Descargar PostgreSQL 14.11](https://www.enterprisedb.com/download-postgresql-binaries).

Una vez descargado, sigue estos pasos:

1. Descomprime el archivo descargado.
2. Dentro de la carpeta descomprimida, crea un archivo `.bat`. Por ejemplo, `servicio.bat`.
3. Abre el archivo `.bat` con un editor de texto y añade el siguiente contenido:

```batch
@echo off
@SET PATH="%~dp0\bin";%PATH%
@SET PGDATA=%~dp0\data
@SET PGDATABASE=postgres
@SET PGUSER=postgres
@SET PGPORT=5435
@SET PGLOCALEDIR=%~dp0\share\locale
rem "%~dp0\bin\initdb" -U postgres -A trust
"%~dp0\bin\pg_ctl" -D "%~dp0/data" -l logfile start
ECHO "Presiona enter para detener el servicio"
pause
"%~dp0\bin\pg_ctl" -D "%~dp0/data" stop
```

4. Guarda el archivo `.bat`.

5. Ejecuta el archivo `.bat` y luego prueba que todo funcione correctamente desde la consola.

En este caso, se utiliza el puerto `5435`. Asegúrate de que este puerto esté disponible y no esté siendo utilizado por otro servicio en tu sistema.


## Proyecto Django

Este proyecto Django requiere una estructura específica de carpetas. Sigue estos pasos para configurarlo:

1. Crea una carpeta principal para tu proyecto Django.

2. Dentro de la carpeta principal, crea otra carpeta llamada `app`.

3. Clona el proyecto dentro de la carpeta `app`. Si al clonar el proyecto se crea una carpeta adicional, mueve todos los archivos que estén dentro de esa carpeta al directorio `app`.

Una vez que hayas configurado la estructura de carpetas, sigue los siguientes pasos para configurar el entorno virtual y ejecutar el proyecto:

1. Crea un entorno virtual. Puedes usar el siguiente comando en la terminal:

   ```bash
   python -m venv venv
   ```

2. Activa el entorno virtual. En Windows, puedes hacerlo con el siguiente comando:

   ```bash
   venv\Scripts\activate
   ```

3. Instala los requerimientos del proyecto utilizando `pip`. Asegúrate de estar en el directorio principal del proyecto donde se encuentra el archivo `requirements.txt` y ejecuta:

   ```bash
   pip install -r requirements.txt
   ```

4. Una vez instalados los requerimientos, asegúrate de tener configurada la base de datos. Si necesitas configurarla, ajusta el archivo `settings.py` de Django según sea necesario.

5. Inicia el servidor de desarrollo de Django con el siguiente comando:

   ```bash
   python manage.py runserver
   ```

6. Ahora puedes acceder al proyecto en tu navegador a través de la dirección proporcionada por el servidor de desarrollo de Django.

## Listar Datos desde la API de la Tabla Productos

Antes de listar los datos desde la API de la tabla de productos, asegúrate de haber ejecutado correctamente el proyecto. Puedes hacerlo ejecutando el servidor de desarrollo de Django con el siguiente comando:

```bash
python manage.py runserver
```

Una vez que el servidor esté en funcionamiento, sigue estos pasos:

1. Abre tu navegador web o Postman.

2. Ingresa a la siguiente ruta: `http://127.0.0.1:8000/api/productos/`.

3. Asegúrate de hacer una solicitud utilizando el método HTTP GET.

4. Si estás utilizando el navegador, verás una representación de los datos en formato JSON directamente en la página.

5. Si estás utilizando Postman, la respuesta será mostrada de manera estructurada y más legible.

Al realizar esta solicitud, obtendrás una lista de los datos de la tabla de productos disponibles en el sistema a través de la API. Esto te permitirá visualizar la información y realizar cualquier acción adicional según tus necesidades.

## Docker: Ejecución del Proyecto

Para ejecutar mi proyecto utilizando Docker, sigo estos pasos:

1. Aseguro tener mi entorno virtual activado.

2. Ejecuto el siguiente comando desde la consola para construir y levantar los contenedores:

```bash
docker-compose up -d --build
```

Este comando inicia la construcción de los contenedores Docker según las configuraciones definidas en mis archivos `Dockerfile`, `docker-compose.yml`, `entrypoint`, y `command`.

3. Una vez que la construcción ha finalizado correctamente, mis contenedores están en funcionamiento.

Sin embargo, he notado que al intentar iniciar mi proyecto desde los contenedores de Docker, me encuentro con algunos errores. Aunque los contenedores se crean correctamente y parecen funcionar, estos errores deben ser resueltos para asegurar un funcionamiento óptimo del proyecto en el entorno Dockerizado.

Investigaré estos errores para identificar sus causas y realizaré las correcciones necesarias en los archivos Docker relacionados. Revisaré los registros de los contenedores para entender mejor el origen de los problemas y tomar las acciones correctivas adecuadas.

Una vez que haya solucionado estos errores, podré garantizar que mi proyecto se ejecute de manera adecuada dentro de los contenedores Docker.

## Ajax 