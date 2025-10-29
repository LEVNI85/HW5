from django.urls import path
from . import views

urlpatterns = [
    path('course/', views.create_course, name='create_course'),
    path('student/', views.create_student, name='create_student'),
    path('success/', views.success, name='success'),
    path('displaycourses/', views.display_course, name='displayC'),
    path('displaystudents/', views.display_student, name='displayS')
]
