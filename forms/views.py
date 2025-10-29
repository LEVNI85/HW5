from django.shortcuts import render, redirect
from .forms import CourseForm, StudentModelForm
from .models import Course, Student

def create_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            Course.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description']
            )
            return redirect('success')  
    else:
        form = CourseForm()
    return render(request, 'course.html', {'form': form})


def create_student(request):
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('success')  
    else:
        form = StudentModelForm()
    return render(request, 'student.html', {'form': form})

def display_course(request):
    courses = Course.objects.all()  
    return render(request, 'displayC.html', {'courses': courses})

def display_student(request):
    students = Student.objects.all()  
    return render(request, 'displayS.html', {'students': students})

def success(request):
    return render(request, 'success.html')

