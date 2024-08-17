# Clonar el proyecto (si es necesario)
git clone https://github.com/usuario/proyecto-django.git](https://github.com/richiparada/SICOAP.git
cd proyecto-django

# Crear y activar el entorno virtual
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Aplicar migraciones
python manage.py migrate

# Crear superusuario (opcional)
python manage.py createsuperuser

# Ejecutar el servidor de desarrollo
python manage.py runserver
