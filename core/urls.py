from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='inicio.html'), name='home'),
    path('animais/', views.lista_animais, name='lista_animais'),
    path('agendar_consulta/', views.agendar_consulta, name='agendar_consulta'),
    path('consultas/', views.lista_consultas, name='lista_consultas'),
]
