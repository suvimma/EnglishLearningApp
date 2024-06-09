# English Learning App

English Learning App to aplikacja webowa s³u¿¹ca do nauki jêzyka angielskiego poprzez fiszki, gry pamiêciowe oraz testy.

## Instalacja

### Klonowanie repozytorium

1. Skopiuj repozytorium:
   ```bash
   git clone https://github.com/suvimma/EnglishLearningApp.git
   cd EnglishLearningApp

2. Konfiguracja œrodowiska wirtualnego
Utwórz i aktywuj wirtualne œrodowisko:


python -m venv venv
source venv/bin/activate  # Dla systemów Unix
.\venv\Scripts\activate   # Dla systemów Windows

3.Instalacja zale¿noœci
Zainstaluj zale¿noœci:

pip install -r requirements.txt

4.Konfiguracja bazy danych

Skonfiguruj bazê danych w pliku settings.py (dostosuj ustawienia bazy danych wed³ug potrzeb).

5.Migracje bazy danych

PrzeprowadŸ migracje bazy danych:

python manage.py migrate

6.Uruchomienie serwera

Uruchom serwer:

python manage.py runserver

U¿ycie
Po uruchomieniu serwera przejdŸ do http://127.0.0.1:8000/ w przegl¹darce, aby zobaczyæ aplikacjê.

Wk³ad
Chêtnie przyjmujemy wk³ad w rozwój projektu. Mo¿esz zg³aszaæ b³êdy i propozycje nowych funkcji poprzez Issues na GitHubie.

Licencja
Ten projekt jest licencjonowany na zasadach licencji MIT. Szczegó³y znajduj¹ siê w pliku LICENSE.

Weryfikacja pliku requirements.txt
Upewnij siê, ¿e plik requirements.txt zawiera wszystkie niezbêdne zale¿noœci. Poni¿ej znajduje siê przyk³ad pliku requirements.txt, który powinien obejmowaæ wszystkie potrzebne pakiety:

Django==3.2.9
django-axes==5.25.0
django-captcha==0.5.13
mssql-django==1.0
pyodbc==4.0.32

Finalizacja na GitHubie
Upewnij siê, ¿e plik README.md i requirements.txt znajduj¹ siê w repozytorium na GitHubie.

Jeœli wprowadzi³eœ jakiekolwiek zmiany, wykonaj commit i push tych zmian:

git add README.md requirements.txt
git commit -m "Update README.md and requirements.txt"
git push origin master

