import logging
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from .forms import UserRegisterForm, UserLoginForm
from django.http import HttpResponse
from .fetch_words import fetch_words
from .models import Flashcard
from .forms import FlashcardForm
from .models import Word
import random
import json
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.html import escape

# Konfiguracja logowania
logger = logging.getLogger(__name__)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = escape(form.cleaned_data.get('username'))  # Escapowanie danych
            basic_group = Group.objects.get(name='BasicUser')
            user.groups.add(basic_group)
            messages.success(request, f'Account created for {username}! Please log in.')
            logger.info(f'Account created for {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'flashcards/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = escape(form.cleaned_data.get('username'))  # Escapowanie danych
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)  
                logger.info(f"User {username} logged in.")
                return redirect('level')
            else:
                messages.error(request, 'Invalid username or password')
                logger.warning(f"Failed login attempt for username: {username}")
    else:
        form = UserLoginForm()
    return render(request, 'flashcards/login.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    logger.info(f"User {request.user.username} logged out.")
    return redirect('login')

def update_flashcards(request):
    fetch_words()
    logger.info("Flashcards updated successfully.")
    return HttpResponse("Flashcards updated successfully.")

def flashcard_list(request):
    words = Word.objects.all()
    return render(request, 'flashcards/flashcard_list.html', {'words': words})

@login_required
def select_level(request):
    levels = range(1, 11)
    return render(request, 'flashcards/select_level.html', {'levels': levels})

@login_required
def learn(request, level):
    words = list(Word.objects.filter(level=level).values('english_word', 'polish_word'))
    words_json = json.dumps(words)
    return render(request, 'flashcards/learn.html', {'words_json': words_json})



@login_required
def add_flashcard(request):
    if request.method == 'POST':
        english_word = request.POST['english_word']
        polish_word = request.POST['polish_word']
        level = request.POST['level']
        Word.objects.create(english_word=english_word, polish_word=polish_word, level=level)
        logger.info(f"Flashcard added: {english_word} - {polish_word}")
    return render(request, 'flashcards/add_flashcard.html')

@login_required
def choose_level(request):
    sets = range(1, 11)
    return render(request, 'flashcards/choose_level.html', {'sets': sets})

@login_required
def memory_game(request, set_number, level):
    start_index = (set_number - 1) * 100
    end_index = set_number * 100
    words = list(Word.objects.all()[start_index:end_index])

    if not words:
        logger.error(f"No words found for set {set_number} and level {level}.")
        return render(request, 'flashcards/error.html', {'message': 'No words found for this set.'})

    if level == 1:
        selected_words = random.sample(words, 6)  # 3 pary
        grid_size = 3
    elif level == 2:
        selected_words = random.sample(words, 8)  # 4 pary
        grid_size = 4
    elif level == 3:
        selected_words = random.sample(words, 10) # 5 pary
        grid_size = 5

    context = {
        'words': selected_words,
        'set_number': set_number,
        'level': level,
        'grid_size': grid_size,
    }
    logger.info(f"Memory game started: set {set_number}, level {level}.")
    return render(request, 'flashcards/memory_game.html', context)

def handle_uploaded_file(f):
    if f.content_type not in ['image/jpeg', 'image/png']:
        raise ValidationError('Unsupported file type.')
    if f.size > 5 * 1024 * 1024:
        raise ValidationError('File too large.')

@login_required
def level_view(request):
    levels = range(1, 11)  # Assuming 10 levels
    return render(request, 'flashcards/level.html', {'levels': levels})

@login_required
def learn_view(request, level):
    words = Flashcard.objects.filter(level=level).values('english_word', 'polish_word')
    words_json = json.dumps(list(words))
    return render(request, 'flashcards/learn.html', {'words_json': words_json})

@login_required
def select_test_level(request):
    levels = range(1, 11)
    return render(request, 'flashcards/select_test_level.html', {'levels': levels})

@login_required
def test_view(request, level):
    words = list(Word.objects.filter(level=level))
    if len(words) > 10:
        words = random.sample(words, 10)
    return render(request, 'flashcards/test.html', {'words': words})

@login_required
def submit_test(request):
    if request.method == 'POST':
        answers = request.POST.getlist('answer')
        questions = request.POST.getlist('question')
        correct_answers = 0
        total_questions = len(questions)

        for question, answer in zip(questions, answers):
            words = Word.objects.filter(english_word=question)
            if any(word.polish_word.lower() == answer.strip().lower() for word in words):
                correct_answers += 1

        score = (correct_answers / total_questions) * 100
        logger.info(f"Test submitted. Score: {score}%")
        return render(request, 'flashcards/test_result.html', {'score': score, 'correct_answers': correct_answers, 'total_questions': total_questions})

    return redirect('select_test_level')

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        username = user.username
        user.delete()
        logger.info(f"User {username} has been deleted.")
        messages.success(request, 'Your account has been deleted.')
        return redirect('home')
    return render(request, 'flashcards/delete_account.html')

def locked_view(request):
    return render(request, 'flashcards/locked.html')

def home_view(request):
    return render(request, 'home.html')