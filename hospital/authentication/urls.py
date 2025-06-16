from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='signin'),
    path('register/', views.UserRegisterView.as_view(), name='signup'),
    
    
    path('addpatient/', views.AddPatient.as_view(), name='addpatient')
]
