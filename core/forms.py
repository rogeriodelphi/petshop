from django import forms
from .models import Consulta

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['animal', 'veterinario', 'data', 'motivo', 'observacoes']
        widgets = {
            'data': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        data = cleaned_data.get('data')
        veterinario = cleaned_data.get('veterinario')
        print(data, veterinario)




        # Garante que ambos os campos existem antes de tentar a consulta
        if data and veterinario:
            # Exclui a própria instância se estivermos editando uma consulta existente
            # Isso evita que o formulário dê erro ao salvar uma edição sem alterar o horário.
            qs = Consulta.objects.filter(data=data, veterinario=veterinario)
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)

            if qs.exists():
            # Esta é a forma padrão de adicionar um erro a um campo específico ou ao formulário geral.
                raise forms.ValidationError(
                    'Já existe uma consulta agendada neste horário para este veterinário.'
                )
        return cleaned_data