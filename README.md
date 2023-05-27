## Instalación

Para ejecutar la aplicación en un entorno local se debe instalar los paquetes usando pip, configurar un entorno virtual, activarlo y posteriormente lanzar el script que inicia el servidor local

```bash
# estando en la raíz:

    pip install requirements.txt

# crear y activar entorno virtual

    python -m venv .venv

  #hecho con una maquina con linux

    source .venv/bin/activate 

# lanzar la app

    cd src && python manage.py runserver

```

La aplicación tiene 3 modelos de datos, en los 3 pueden insertarse datos accediendo primero desde un link en el nav bar que comparten todos los templates.

## Django root

user -> admin.

contraseña -> 1234
