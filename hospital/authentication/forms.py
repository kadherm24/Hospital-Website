# importing the inbuilt User model from django.contrib.auth
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Patient

class CustomRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields
    username = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class' : 'form-control', 'placeholder': 'Enter Your Username'
            }
        )
    )

    password1 = forms.CharField(
        label= 'Password',
        widget= forms.PasswordInput(
            attrs={
                'class':'form-control', 'placeholder' : 'Enter Your Password.'
            }
        )

    )
    password2 = forms.CharField(
        label= 'Confirm Password',
        widget= forms.PasswordInput(
            attrs={
                'class':'form-control', 'placeholder' : 'Confirm Your Password.'
            }
        )

    )


class CustomLoginForm(AuthenticationForm):
     username = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class' : 'form-control', 'placeholder': 'Enter Your Username'
            }
        )
    )
     
     password = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                'class':'form-control', 'placeholder' : 'Enter Your Password.'
            }
        )

    )



class AddPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = ['user']


