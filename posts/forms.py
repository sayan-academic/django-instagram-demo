from django import forms

from .models import *
from django.utils import timezone


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
    class Media:
        css = {'all': ('posts/postform.css',)}
        js = ('posts/postform.js',)