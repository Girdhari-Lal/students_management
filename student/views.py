from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentUploadForm, StudentEditForm
import pandas as pd
from .models import Student
import random
import string

def generate_username(name):
    return name.lower().replace(" ", "") + ''.join(random.choices(string.digits, k=4))

def upload_student_data(request):
    if request.method == 'POST':
        form = StudentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            try:
                # Check file extension
                filename = uploaded_file.name.lower()
                if filename.endswith('.csv'):
                    df = pd.read_csv(uploaded_file)
                elif filename.endswith(('.xls', '.xlsx')):
                    df = pd.read_excel(uploaded_file)
                else:
                    df = None

                if df is not None:
                    for index, row in df.iterrows():
                        username = generate_username(row['name'])
                        Student.objects.create(
                            name=row['name'],
                            age=int(row['age']),
                            address=row['address'],
                            email=row['email'],
                            username=username
                        )
                    return redirect('dashboard')

            except Exception as e:
                print("Error reading file:", e)

            return render(request, 'upload.html',{'form': form})
    else:
        form = StudentUploadForm()

    return render(request, 'upload.html', {'form': form})

def student_dashboard(request):
    students = Student.objects.all()
    return render(request, 'dashboard.html', {'students': students})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('dashboard')

def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentEditForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = StudentEditForm(instance=student)
    return render(request, 'edit.html', {'form': form, 'student': student})