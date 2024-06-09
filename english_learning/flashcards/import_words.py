# -*- coding: utf-8 -*-

import os
import django
import csv
 
# Ustawienia Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "english_learning.settings")
django.setup()

from flashcards.models import Word

def import_words_from_csv():
    csv_file_path = os.path.join(os.path.dirname(__file__), 'words.csv')
    words = []
    with open(csv_file_path, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            words.append((row['English Word'], row['Polish Word']))
    return words

def determine_level_and_category(word):
    # Przyk³adowa logika przypisywania kategorii i poziomów
    common_words = ["good", "teacher", "mirror", "window"]
    if word.lower() in common_words:
        return "Beginner", "Basic Vocabulary"
    else:
        return "Advanced", "Advanced Vocabulary"

def import_words():
    words = import_words_from_csv()  # Zak³adamy, ¿e fetch_words_from_wiktionary() zwraca listê s³ów
    set_size = 100  # Rozmiar zestawu
    set_number = 1  # Numer zestawu

    for index, (english_word, polish_word) in enumerate(words):
        level, category = determine_level_and_category(english_word)
        if index % set_size == 0 and index != 0:
            set_number += 1

        Word.objects.get_or_create(
            english_word=english_word,
            polish_word=polish_word,
            defaults={'level': level, 'category': category, 'set_number': set_number}
        )
        Word.objects.get_or_create(
            english_word=polish_word,
            polish_word=english_word,
            defaults={'level': level, 'category': category, 'set_number': set_number}  # odwrotna para
        )

# Uruchomienie skryptu
if __name__ == "__main__":
    import_words()
