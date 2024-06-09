
# English Learning App

English Learning App to aplikacja webowa służąca do nauki języka angielskiego poprzez fiszki, gry pamięciowe oraz testy.

## Instalacja

### Klonowanie repozytorium

1. Skopiuj repozytorium:
   ```bash
   git clone https://github.com/suvimma/EnglishLearningApp.git
   cd EnglishLearningApp

2. Konfiguracja środowiska wirtualnego
Utwórz i aktywuj wirtualne środowisko:


python -m venv venv
source venv/bin/activate  # Dla systemów Unix
.\venv\Scripts\activate   # Dla systemów Windows

3.Instalacja zależności
Zainstaluj zależności:

pip install -r requirements.txt

4.Konfiguracja bazy danych

Skonfiguruj bazę danych w pliku settings.py (dostosuj ustawienia bazy danych według potrzeb).

5.Migracje bazy danych

Przeprowadź migracje bazy danych:

python manage.py migrate

6.Uruchomienie serwera

Uruchom serwer:

python manage.py runserver

Użycie
Po uruchomieniu serwera przejdź do http://127.0.0.1:8000/ w przeglądarce, aby zobaczyć aplikację.

Wkład
Chętnie przyjmujemy wkład w rozwój projektu. Możesz zgłaszać błędy i propozycje nowych funkcji poprzez Issues na GitHubie.

Licencja
Ten projekt jest licencjonowany na zasadach licencji MIT. Szczegóły znajdują się w pliku LICENSE.

Weryfikacja pliku requirements.txt
Upewnij się, że plik requirements.txt zawiera wszystkie niezbędne zależności. Poniżej znajduje się przykład pliku requirements.txt, który powinien obejmować wszystkie potrzebne pakiety:

Django==3.2.9
django-axes==5.25.0
django-captcha==0.5.13
mssql-django==1.0
pyodbc==4.0.32

Finalizacja na GitHubie
Upewnij się, że plik README.md i requirements.txt znajdują się w repozytorium na GitHubie.

Jeśli wprowadziłeś jakiekolwiek zmiany, wykonaj commit i push tych zmian:

git add README.md requirements.txt
git commit -m "Update README.md and requirements.txt"
git push origin master

