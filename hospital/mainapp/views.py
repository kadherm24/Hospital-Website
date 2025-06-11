from django.shortcuts import render
from .models import Doctor
# Create your views here.
def homeView(request):
    docs = Doctor.objects.all() # SELECT * FROM mainapp_doctor;
    context = {
        'doctors' : docs

    }
    template = 'home.html'
    return render(request, template, context) # this renders the response according to the request using the context