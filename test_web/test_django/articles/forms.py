from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     content = forms.CharField(widget=forms.Textarea)
    
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ('created_at', 'updated_at')