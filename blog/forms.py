from django import forms
from .models import Comment, Post

class PostForm(forms.ModelForm):
    # con forms.ModelForm le digo que este formulario es un ModelForm

    class Meta:
        model = Post # le digo que use el modelo Post para crear este formulario
        fields = ('title', 'text',) # campos del formulario

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author','text')