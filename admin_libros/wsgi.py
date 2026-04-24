import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'admin_libros.settings')

# Ejecutar migraciones automáticamente si estamos en Vercel usando SQLite en /tmp
if os.environ.get('VERCEL'):
    from django.core.management import execute_from_command_line
    # Solo intentamos migrar si no hay DATABASE_URL (estamos usando SQLite en /tmp)
    if not os.environ.get('DATABASE_URL'):
        print("Entorno Vercel detectado sin DATABASE_URL. Ejecutando migraciones en /tmp...")
        execute_from_command_line(['manage.py', 'migrate', '--noinput'])

application = get_wsgi_application()
app = application
