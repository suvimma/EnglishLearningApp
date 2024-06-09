# -*- coding: utf-8 -*-

from django.db import models



class Flashcard(models.Model):
    english_word = models.CharField(max_length=100)
    polish_word = models.CharField(max_length=100)
    level = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.english_word} - {self.polish_word}"

class Word(models.Model):
    english_word = models.CharField(max_length=100)
    polish_word = models.CharField(max_length=100)
    level = models.CharField(max_length=50, null=True, blank=True)
    category = models.CharField(max_length=50, null=True, blank=True)
    set_number = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.english_word} - {self.polish_word}"