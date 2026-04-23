# PythonDjangoApp

## Configuración del entorno de desarrollo
1. Crear entorno virtual: `python3 -m venv venv`
2. Activar entorno virtual: `source venv/bin/activate` (Linux) o `venv\Scripts\activate` (Windows)
3. Instalar dependencias: `pip install -r requirements.txt`

## Ejecución del proyecto
1. Ir al directorio del proyecto: `cd proyecto`
2. Realizar migraciones: `python manage.py makemigrations` y `python manage.py migrate`
3. Crear superusuario: `python manage.py createsuperuser`
4. Iniciar servidor: `python manage.py runserver`
