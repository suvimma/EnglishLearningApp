# English Learning App

English Learning App to aplikacja webowa s�u��ca do nauki j�zyka angielskiego poprzez fiszki, gry pami�ciowe oraz testy.

## Instalacja

### Klonowanie repozytorium

1. Skopiuj repozytorium:
   ```bash
   git clone https://github.com/suvimma/EnglishLearningApp.git
   cd EnglishLearningApp

2. Konfiguracja �rodowiska wirtualnego
Utw�rz i aktywuj wirtualne �rodowisko:


python -m venv venv
source venv/bin/activate  # Dla system�w Unix
.\venv\Scripts\activate   # Dla system�w Windows

3.Instalacja zale�no�ci
Zainstaluj zale�no�ci:

pip install -r requirements.txt

4.Konfiguracja bazy danych

Skonfiguruj baz� danych w pliku settings.py (dostosuj ustawienia bazy danych wed�ug potrzeb).

5.Migracje bazy danych

Przeprowad� migracje bazy danych:

python manage.py migrate

6.Uruchomienie serwera

Uruchom serwer:

python manage.py runserver

U�ycie
Po uruchomieniu serwera przejd� do http://127.0.0.1:8000/ w przegl�darce, aby zobaczy� aplikacj�.

Wk�ad
Ch�tnie przyjmujemy wk�ad w rozw�j projektu. Mo�esz zg�asza� b��dy i propozycje nowych funkcji poprzez Issues na GitHubie.

Licencja
Ten projekt jest licencjonowany na zasadach licencji MIT. Szczeg�y znajduj� si� w pliku LICENSE.

Weryfikacja pliku requirements.txt
Upewnij si�, �e plik requirements.txt zawiera wszystkie niezb�dne zale�no�ci. Poni�ej znajduje si� przyk�ad pliku requirements.txt, kt�ry powinien obejmowa� wszystkie potrzebne pakiety:

Django==3.2.9
django-axes==5.25.0
django-captcha==0.5.13
mssql-django==1.0
pyodbc==4.0.32

Finalizacja na GitHubie
Upewnij si�, �e plik README.md i requirements.txt znajduj� si� w repozytorium na GitHubie.

Je�li wprowadzi�e� jakiekolwiek zmiany, wykonaj commit i push tych zmian:

git add README.md requirements.txt
git commit -m "Update README.md and requirements.txt"
git push origin master

