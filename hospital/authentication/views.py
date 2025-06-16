from django.shortcuts import render

# importing the inbuilt User model
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from .models import Patient
from django.urls import reverse_lazy # finds the url path associated with a url name

from django.views.generic import CreateView, ListView

from .forms import CustomLoginForm, CustomRegistrationForm, AddPatientForm


# Create your views here.
#Authentication 
class CustomLoginView(LoginView):
    template_name = 'signin.html'
    form_class  = CustomLoginForm
    

class UserRegisterView(CreateView):
    model = User 
    form_class = CustomRegistrationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('signin')# redirects user to login page after registeration

#CRUD operations for Patient
#1. Create View
class AddPatient(CreateView):
    form_class = AddPatientForm
    model = Patient 
    template_name = 'add_patient.html'
    success_url = '/'


    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)
    
    
