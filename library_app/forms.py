from django import forms
from library_app import models
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

User = get_user_model()


class BookModelForm(forms.ModelForm):

    class Meta():

        model = models.BOOK
        fields = ('Book_name','Book_description','Category','Book_type','Price')




#############################################################



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}

