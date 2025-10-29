from django import forms
from .models import Student, Course

class CourseForm(forms.Form):
    name = forms.CharField(max_length=100, label="Course Name")
    description = forms.CharField(label="Course Description")

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_n', 'last_n']
