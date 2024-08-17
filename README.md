git clone https://github.com/richiparada/SICOAP.git
cd SICOAP
  En windows usar el comando 
    python -m venv venv
  En linux o mac
    source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
