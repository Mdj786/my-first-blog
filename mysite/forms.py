from django import forms
from .models import Post

class HomeForm(forms.Form):
     title = models.CharField(max_length=200)
     text = models.TextField()

     class Meta:
          model = Post
          fields = ('title','text')
