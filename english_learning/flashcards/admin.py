from django.contrib import admin
from .models import Flashcard, Word

# Usu� duplikaty rejestracji, je�li istniej�
class FlashcardAdmin(admin.ModelAdmin):
    list_display = ('english_word', 'polish_word', 'level')

admin.site.register(Flashcard, FlashcardAdmin)
admin.site.register(Word)  # Dodaj tylko je�li nie jest ju� zarejestrowany
