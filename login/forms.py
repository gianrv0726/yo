from django import forms
from django.contrib.auth.models import User


#class UserForm(forms.ModelForm):
#    password = forms.CharField(widget=forms.PasswordInput)
#
#    class Meta:
#        model = User
#        fields = ['username', 'email', 'password']

class UserForm(forms.ModelForm):
    #corr = forms.CharField(max_length=40, required=True,label="", widget=(forms.TextInput(attrs={"placeholder":"Correo Electronico","class":"input-register"})))
    #nom = forms.CharField(max_length=40, required=True,label="", widget=(forms.TextInput(attrs={"placeholder":"Nombre","class":"input-register"})))
    #cont = forms.CharField(max_length=20, required=True,label="", widget=(forms.PasswordInput(attrs={"placeholder":"Contraseña","class":"input-register"})))
    class Meta:
            model = User
            fields = ['username', 'first_name', 'last_name', 'email', 'password']
