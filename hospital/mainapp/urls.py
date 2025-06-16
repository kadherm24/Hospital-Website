from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name = 'homepage'),
    path('doctor/<int:pk>', views.DoctorDetails.as_view(), name = 'doc_detail'),
    path('doctor/add', views.AddDoctor.as_view(), name = 'add_doc'),
    path('doctor/edit/<int:pk>', views.EditDoctor.as_view(), name = 'edit_doc'),
    path('doctor/del/<int:pk>', views.DeleteDoctor.as_view(), name = 'del_doc'),


    path('categories/', views.specialities, name = 'specs'),
    path('carousel/', views.carousel, name='caros')

]