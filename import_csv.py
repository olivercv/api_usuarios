import csv
import os
import django
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api_usuarios.settings")
django.setup()

from usuarios.models import Usuario

def import_users(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            Usuario.objects.create(
                nombre=row['Nombre'],
                apellidoPaterno=row['Apellido paterno'],
                apellidoMaterno=row['Apellido materno'],
                edad=int(row['Edad']),
                nombreCuenta=row['Nombre de la cuenta'],
                contrasena=row['Contraseña']
            )

if __name__ == "__main__":
    import_users('usuarios.csv')
    