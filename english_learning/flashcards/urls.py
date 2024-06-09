from django.urls import path
from . import views

urlpatterns = [
    path('', views.level_view, name='level'),
    path('learn/<int:level>/', views.learn, name='learn'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add_flashcard/', views.add_flashcard, name='add_flashcard'),
    path('choose_level/', views.choose_level, name='choose_level'),
    path('memory_game/<int:set_number>/<int:level>/', views.memory_game, name='memory_game'),
    path('flashcard_list/', views.flashcard_list, name='flashcard_list'),
    path('select_test_level/', views.select_test_level, name='select_test_level'),
    path('test/<int:level>/', views.test_view, name='test_view'),
    path('submit_test/', views.submit_test, name='submit_test'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('locked/', views.locked_view, name='locked'),
]
