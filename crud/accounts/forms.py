from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from .models import Tipo_proveedor

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields= [
            'username',
            'email',
            'password1',
            'password2',
        ]
'''
class SignUpCompleteForm(forms.ModelForm):
    class Meta:
        model = User
        fields= [
            'username',
            'email',
            'password1',
            'password2',
        ]'''
"""
class SignInForm():
    class Meta:
        model = User
        fields= [
            'username',
            'password',
        ]
"""