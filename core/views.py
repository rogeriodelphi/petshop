from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Animal, Consulta
from django.core.exceptions import ValidationError
from .forms import ConsultaForm

def lista_animais(request):
    animais = Animal.objects.all()
    return render(request, 'lista_animais.html', {'animais': animais})


# Agendar consulta
def agendar_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        # print('Dado do formulário', form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Consulta agendada com sucesso!')
            # return redirect('lista_consultas')
        else:
            form._errors.clear() # remove os erros anteriores
            form.add_error(None, 'Erro ao agendar consulta.')
            messages.error(request, 'Erro ao agendar consultar.')
    else:
        form = ConsultaForm()
    return render(request, 'agendar_consulta.html', {'form': form})

def lista_consultas(request):
    consultas = Consulta.objects.all().order_by('data')
    return render(request, 'lista_consultas.html', {'consultas': consultas})
