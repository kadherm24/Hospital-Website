from django.shortcuts import render

# importing the inbuilt User model
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from .models import Patient
from django.urls import reverse_lazy # finds the url path associated with a url name

from django.views.generic import CreateView, ListView, DeleteView, UpdateView,  DetailView

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
    
#2.Read
#ListView
def patientView(request):
    patient = Patient.objects.filter(user = request.user) # SELECT * FROM patient;
    context = {
        'patients' : patient

    }
    template = 'patients.html'
    return render(request, template, context)

#Detailview
class PatientDetails(DetailView):
    model = Patient
    template_name = 'patient_details.html'
    context_object_name = 'patient'
    success_url = '/'


class EditPatient(UpdateView):
    model = Patient
    fields = '__all__'
    template_name = 'edit_patient.html'
    success_url = '/'

# 4. Delete view (Delete statement)
class DeletePatient(DeleteView):
    model = Patient
    template_name = 'delete_patient.html'
    success_url = '/'

    
    
