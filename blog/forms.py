from django import forms
from .models import Post


class NewForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'author', 'status', ]

