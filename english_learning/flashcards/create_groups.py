# flashcards/create_groups.py
from django.contrib.auth.models import Group

def create_groups():
    # Tworzenie grupy BasicUser jeœli nie istnieje
    group, created = Group.objects.get_or_create(name='BasicUser')
    if created:
        print("Group 'BasicUser' created.")
    else:
        print("Group 'BasicUser' already exists.")
