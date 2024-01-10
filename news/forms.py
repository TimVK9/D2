from django import forms
from django.core.exceptions import ValidationError

from .models import Post, Author


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title',
                  'text',
                  'author',
                  'postCategory'

                  ]

        labels = {
            'title': 'Заголовок',
            'text': 'Текст',
            'postCategory': 'Категория'

        }

