from django import forms
from .models import Snippet, Comment


class SnippetForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['code'].required = False

    class Meta:
        model = Snippet
        fields = ['title', 'code', 'category', 'technology']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'bg-zinc-900 text-white px-4 py-2 rounded focus:outline-none focus:ring-2 focus:ring-green-400 border border-transparent hover:border-white transition'
            }),
            'code': forms.Textarea(attrs={'rows' : 10, 'cols': 80
            }),
            'category': forms.TextInput(attrs={
                'class': 'bg-zinc-900 text-white px-4 py-2 rounded focus:outline-none focus:ring-2 focus:ring-green-400 border border-transparent hover:border-white transition'
            }),
            'technology': forms.TextInput(attrs={
                'class': 'bg-zinc-900 text-white px-4 py-2 rounded focus:outline-none focus:ring-2 focus:ring-green-400 border border-transparent hover:border-white transition'
            }),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'bg-zinc-900 text-white px-4 py-2 rounded focus:outline-none focus:ring-2 focus:ring-green-400 border border-transparent hover:border-white transition'
            })
        }