from django.contrib import admin
from .models import Flashcard, Word

# Usuñ duplikaty rejestracji, jeœli istniej¹
class FlashcardAdmin(admin.ModelAdmin):
    list_display = ('english_word', 'polish_word', 'level')

admin.site.register(Flashcard, FlashcardAdmin)
admin.site.register(Word)  # Dodaj tylko jeœli nie jest ju¿ zarejestrowany
