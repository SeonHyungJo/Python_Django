from django import forms
from .models import GuessNumbers
# 모델클래스 GuessNumbers로 부터 데이터를 입력 받을 폼을 작성한다.


class PostForm(forms.ModelForm):
    class Meta:
        model = GuessNumbers
        fields = ('name', 'text', 'num_lotto')
