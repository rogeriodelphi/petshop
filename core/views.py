from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Animal, Consulta
from django.core.exceptions import ValidationError
from .forms import ConsultaForm



def lista_animais(request):
    animais = Animal.objects.all()
    return render(request, 'lista_animais.html', {'animais': animais})


def agendar_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Consulta agendada com sucesso!')
                return redirect('lista_consultas')
            except ValidationError as e:
                messages.error(request, e.message)
    else:
        form = ConsultaForm()
    return render(request, 'agendar_consulta.html', {'form': form})


def lista_consultas(request):
    consultas = Consulta.objects.all().order_by('data')
    return render(request, 'lista_consultas.html', {'consultas': consultas})
