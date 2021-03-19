from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    title = forms.CharField(
        label='영화제목',
        widget= forms.TextInput(
            attrs={
                'class': 'form-control',
                'place_holder': '제목을 입력해주세요',
                'maxlength': 100,
            }
        )
    )
    overview = forms.CharField(
        label='줄거리',
        widget=forms.Textarea(
            attrs={
                'class' : 'form-control',
                'place_holder': '줄거리를 입력해주세요',
            }
        )
    )

    poster_path = forms.CharField(
        label='포스터',
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'place_holder': '파일경로를 입력해주세요',
                'maxlength': 500,
            }
        )
    )
    class Meta:
        model = Movie
        fields = '__all__'