from . import views
from django.urls import path

app_name = 'patient'
urlpatterns = [

    path('patientProfile/', views.patientProfile, name='patientProfile'),
    path('patientRecords/', views.patientRecords, name='patientRecords'),
    path('personalNotes/', views.personalNotes, name='personalNotes'),
    
    # path('login/',views.login,name ='login'),
    path('registerpage/',views.registerpage,name ='registerpage'),
    path('signup/',views.signup, name ='signup'),
    path('loginp/',views.loginn, name ='loginp'),
    path('logout/',views.logout, name ='logout'),

]
