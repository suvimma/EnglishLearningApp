#  obraz Python jako bazowy
FROM python:3.12

# Ustaw katalog roboczy w kontenerze
WORKDIR /app

# Skopiuj plik requirements.txt do katalogu roboczego
COPY requirements.txt /app/

# Zainstaluj zale¿noœci
RUN pip install --no-cache-dir -r requirements.txt

# Skopiuj resztê kodu aplikacji do katalogu roboczego
COPY . /app/

# Ustaw zmienne œrodowiskowe
ENV DJANGO_SETTINGS_MODULE=english_learning.settings
ENV PYTHONUNBUFFERED=1

# Uruchom migracje i startuj serwer Django
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
