# Generated by Django 5.0.6 on 2024-06-06 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0005_word_set_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='flashcard',
            name='level',
            field=models.IntegerField(default=1),
        ),
    ]
