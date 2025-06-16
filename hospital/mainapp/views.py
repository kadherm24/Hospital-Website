from django.shortcuts import render
from .models import Doctor

# Importing generic Class Based Views (CBV)
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
# Create your views here.


# CRUD operations of Doctor model

# 1. Create (Insert statements)
class AddDoctor(CreateView):
    model = Doctor
    fields = '__all__'
    template_name = 'add_doctor.html'
    success_url = '/'


#2. Read (Select Statements)

#ListView
def homeView(request):
    docs = Doctor.objects.all() # SELECT * FROM mainapp_doctor;
    context = {
        'doctors' : docs

    }
    template = 'home.html'
    return render(request, template, context) # this renders the response according to the request using the context

#Detialview
class DoctorDetails(DetailView):
    model = Doctor
    template_name = 'doctor_details.html'
    context_object_name = 'doctor'
    success_url = '/'
    

# 3. Update view (Update statement)
class EditDoctor(UpdateView):
    model = Doctor
    fields = '__all__'
    template_name = 'edit_doctor.html'
    success_url = '/'

# 4. Delete view (Delete statement)
class DeleteDoctor(DeleteView):
    model = Doctor
    template_name = 'delete_doctor.html'
    success_url = '/'


def specialities(request):
    template = 'specialities.html'

    context = {
        'specs' : Doctor.CATEGORY_CHOICES
    }

    return render(request, template, context)

def carousel(request):
    caros = Doctor.objects.all() # SELECT * FROM mainapp_doctor;
    context = {
        'carousels' : caros
    }
    template = 'carousel.html'
    return render(request, template, context) # this renders the response according to the request using the context

