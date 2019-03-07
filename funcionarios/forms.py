from django import forms
from .models import Funcionario


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = {'name', 'email','department'}

