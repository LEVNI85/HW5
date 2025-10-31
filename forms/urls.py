from django.urls import path
from . import views

urlpatterns = [
    path('course/', views.create_course, name='create_course'),
    path('student/', views.create_student, name='create_student'),
    path('success/', views.success, name='success'),
    path('displaycourses/', views.display_course, name='displayC'),
    path('displaystudents/', views.display_student, name='displayS'),
    path('subject/', views.create_subject, name='create_subject'),
    path('subject/edit/<int:id>/', views.subject_edit, name='subject_edit'),
    path('subject/delete/<int:id>/', views.subject_delete, name='subject_delete')
]
