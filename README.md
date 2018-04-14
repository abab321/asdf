instaliraj https://www.python.org/downloads/release/python-365/

kloniraj ovaj projekt

- python3 -m venv venv

- source venv/bin/activate

- pip install -r requirements.txt

- cd backend

- python3 manage.py migrate

- python3 manage.py createsuperuser

- python3 manage.py runserver

voila

puni bazu, testiraj

localhost:8000/admin je nesto a la cms za ubacivanje sadrzaja

localhost:8000/api su ti linkovi iz kojih vuces za frontend ( sve je GET osim api/kontakt koji je POST)
