from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='signin'),
    path('register/', views.UserRegisterView.as_view(), name='signup'),
    
    
    path('addpatient/', views.AddPatient.as_view(), name='addpatient'),
    path('patientview/', views.patientView, name='patientview'),
    path('patient/<int:pk>', views.PatientDetails.as_view(), name = 'patient_detail'),
    path('patient/edit/<int:pk>', views.EditPatient.as_view(), name = 'edit_patient'),
    path('patient/del/<int:pk>', views.DeletePatient.as_view(), name = 'del_patient'),
]
