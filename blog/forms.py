from django import forms

from .models import Comment
import random

random_names = ['Golfinho Anônimo', 'Tubarão Anônimo', 'Baleia Anônima', 'Peixe Anônimo', 'Polvo Anônimo', 
                'Estrela do Mar Anônima', 'Água Viva Anônima', 'Cavalo Marinho Anônimo', 'Caranguejo Anônimo', 
                'Lula Anônima', 'Siri Anônimo', 'Concha Anônima', 'Alga Anônima', 'Coral Anônimo', 'Tartaruga Anônima', 
                'Mergulhador Anônimo', 'Sereia Anônima', 'Tubarão Martelo Anônimo', 'Baleia Azul Anônima', 
                'Peixe Palhaço Anônimo', 'Polvo Gigante Anônimo', 'Estrela do Mar Rosa Anônima', 'Água Viva Azul Anônima', 
                'Cavalo Marinho Amarelo Anônimo', 'Caranguejo Vermelho Anônimo', 'Lula Roxa Anônima', 'Siri Azul Anônimo', 
                'Concha Branca Anônima', 'Alga Verde Anônima', 'Coral Vermelho Anônimo', 'Tartaruga Marinha Anônima', 
                'Mergulhador Azul Anônimo', 'Sereia Loira Anônima', 'Tubarão Martelo Cinza Anônimo', 
                'Baleia Azul Gigante Anônima', 'Peixe Palhaço Laranja Anônimo', 'Polvo Gigante Roxo Anônimo', 
                'Estrela do Mar Rosa Choque Anônima', 'Água Viva Azul Marinho Anônima', 'Cavalo Marinho Amarelo Ouro Anônimo', 
                'Caranguejo Vermelho Sangue Anônimo', 'Lula Roxa Fluorescente Anônima', 'Siri Azul Celeste Anônimo', 
                'Concha Branca de Neve Anônima', 'Alga Verde Limão Anônima', 'Coral Vermelho Sangue Anônimo', 
                'Tartaruga Marinha Verde Anônima', 'Mergulhador Azul Marinho Anônimo', 
                'Sereia Loira de Olhos Azuis Anônima', 'Tubarão Martelo Cinza Anônimo']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body', 'email']
        labels = {
            'name': 'Nome',
            'body': 'Comentário',
            'email': '-'
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['email'].initial = 'anom@email.com'
        self.fields['name'].initial = random.choice(random_names)
        self.fields['email'].widget = forms.HiddenInput()
        
        