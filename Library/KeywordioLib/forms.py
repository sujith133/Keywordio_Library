from dataclasses import fields
from django.forms import ModelForm
from .models import logins, book

class loginform(ModelForm):
    class Meta:
        model = logins
        fields= ["useremail","password"]

class Signupform(ModelForm):
    class Meta:
        model = logins
        fields= "__all__"

class book(ModelForm):
    class Meta:
        model = book
        fields= "__all__"