from django import forms
from mysite.models import Post
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#from django.contrib.auth.forms import UserChangeForm
#from .models import CustomUser


class HomeForm(forms.Form):
     title = models.CharField(max_length=200)
     text = models.TextField()

     class Meta:
          model = Post
          fields = ('title','text')
          

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        


'''class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')'''

