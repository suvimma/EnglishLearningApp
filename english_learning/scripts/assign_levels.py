from flashcards.models import Flashcard

def run():
    flashcards = Flashcard.objects.all()
    for i, flashcard in enumerate(flashcards):
        level = (i // 100) + 1
        flashcard.level = level
        flashcard.save()
