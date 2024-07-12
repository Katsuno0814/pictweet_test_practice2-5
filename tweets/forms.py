from .models import Tweet
from django import forms

class TweetForm(forms.ModelForm):
    class Meta:
      model = Tweet
      fields = ['image', 'text']
      widgets = {
         'text': forms.Textarea(attrs={'placeholder': 'Text', 'rows': 10}),
      }
      labels = {
         'text': 'テキスト',
      }

class SearchForm(forms.Form):
    keyword = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': '投稿を検索する',
            'class': 'search-input'
        })
    )