from django import forms

from .models import Comment
import random

random_names = ['Rede Neural Anônima', 'Inteligência Artificial Anônima', 'Deep Learning Anônimo', 'Algoritmo Anônimo',
                'Algoritmo Genético Anônimo', 'Algoritmo de Otimização Anônimo', 'Algoritmo de Classificação Anônimo',
                'Algoritmo de Regressão Anônimo', 'Algoritmo de Clusterização Anônimo', 'Algoritmo de Segmentação Anônimo',
                'Algoritmo de Detecção Anônimo', 'Algoritmo de Reconhecimento Anônimo', 'Algoritmo de Previsão Anônimo',]

random_emails = ['user@aluno.ufop.edu.br']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body', 'email']
        labels = {
            'name': 'Nome (Opcional)',
            'body': 'Comentário *',
            'email': 'E-mail (Opcional)'
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['email'].initial = random.choice(random_emails)
        self.fields['name'].initial = random.choice(random_names)
        
        