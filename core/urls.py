from django.urls import path
from . import views

urlpatterns = [
    path('animais/', views.lista_animais, name='lista_animais'),

]