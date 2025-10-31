from django.shortcuts import render, redirect, get_object_or_404
from .forms import CourseForm, StudentModelForm, SubjectModelForm
from .models import Course, Student, Subject

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

def create_subject(request):
    if request.method == "POST":
        form = SubjectModelForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('create_subject')  
    else:
        form = SubjectModelForm()

    subjects = Subject.objects.all()  
    return render(request, 'subject.html', {'form': form, 'subjects': subjects})

def subject_edit(request, id):
    subject = get_object_or_404(Subject, id=id)

    if request.method == "POST":
        form = SubjectModelForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('create_subject')
    else:
        form = SubjectModelForm(instance=subject)
        
    return render(request, 'subject_edit.html', {'form': form})

def subject_delete(request, id):
    subject = get_object_or_404(Subject, id=id)
    subject.delete()
    return redirect('create_subject')

def display_course(request):
    courses = Course.objects.all()  
    return render(request, 'displayC.html', {'courses': courses})

def display_student(request):
    students = Student.objects.all()  
    return render(request, 'displayS.html', {'students': students})

def success(request):
    return render(request, 'success.html')



