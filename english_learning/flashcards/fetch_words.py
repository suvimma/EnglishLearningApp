
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

def fetch_words():
    url = "https://pl.wiktionary.org/wiki/Indeks:Angielski_-_Polski"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    words = []
    
    for li in soup.find_all('li'):
        text_parts = li.get_text().split()
        if text_parts:  # Sprawd≈∫, czy lista nie jest pusta
            word = text_parts[0]
            words.append(word)
    
    return words
