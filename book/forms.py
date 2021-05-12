from django import forms
from django.forms import ModelForm
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Normal Model Form

#class BookCreateForm(forms.Form):
#    book_name = forms.CharField()
#    auther = forms.CharField()
#    price = forms.IntegerField()
#    pages = forms.IntegerField()




#DJANGO MODEL FORM
class BookCreateForm(ModelForm):
    class Meta:
        model=Book#Book from models.py
        fields="__all__"
 #       widgets={
 #           'book_name':forms.TextInput(attrs={'class':'text_inp','placeholder':'Book Name'})
    #    }


#for registration
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","password1","password2","email"]

#login
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()







