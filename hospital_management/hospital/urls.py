from django.urls import path,include
from . import views
urlpatterns = [

    path('',views.index,name='home'),
    path('about/', views.about,name='about'),
    path('appointment/', views.appointment,name='appointment'),
    path('doctor/', views.doctor,name='doctor'),
    path('patient/', views.patient,name='patient'),
    path('contact/', views.contact,name='contact'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('dashboard/',views. patient_dashboard, name='patient_dashboard'),
    path('patient/<int:patient_id>/', views.patient_detail, name='patient_detail'),
    path('cancel_appointment/<int:appointment_id>/', views.cancel_appointment, name='cancel_appointment'),
    path('confirm_cancel_appointment/<int:appointment_id>/', views.confirm_cancel_appointment, name='confirm_cancel_appointment'),
    path('reschedule_appointment/<int:appointment_id>/', views.reschedule_appointment, name='reschedule_appointment'),
    path('doctor/login', views.doctor_login, name='doctor_login'),
    path('doctor/register', views.doctor_register, name='doctor_register'),
    path('doctor/dashboard/<str:doctor_name>/', views.doctor_dashboard, name='doctor_dashboard'),
    path('create_prescription/', views.create_prescription, name='create_prescription'),
    path('prescription_success/', views.prescription_success, name='prescription_success'),
    path('create-or-edit-medical-record/', views.create_or_edit_medical_record, name='create_or_edit_medical_record'),
    path('success/', views.success_page, name='success_page'),
    path('nurse/register/', views.nurse_register, name='nurse_register'),
    path('nurse/login/', views.nurse_login, name='nurse_login'),
    path('nurse/dashboard/', views.nurse_dashboard, name='nurse_dashboard'),
    path('pharmacist/register/', views.pharmacist_register, name='pharmacist_register'),
    path('pharmacist/login/', views.pharmacist_login, name='pharmacist_login'),
    path('pharmacist/dashboard/', views.pharmacist_dashboard, name='pharmacist_dashboard'),
    path('sign-out/',views.signout,name='logout'),

    # path('department/', views.department,name='department'),
    ]