from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from flashcards import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('flashcards/', include('flashcards.urls')),
    path('', views.home_view, name='home'),  # Strona g³ówna
    path('register/', views.register, name='register'),  
    path('login/', views.login_view, name='login'),  
    path('logout/', views.logout_view, name='logout'),  
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
