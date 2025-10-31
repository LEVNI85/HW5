from django import forms
from .models import Student, Course, Subject

class CourseForm(forms.Form):
    name = forms.CharField(max_length=100, label="Course Name")
    description = forms.CharField(label="Course Description")

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_n', 'last_n']

class SubjectModelForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'number']