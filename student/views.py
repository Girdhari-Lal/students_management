from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentUploadForm, StudentEditForm
import pandas as pd
from .models import Student
import random
import string
from django.http import HttpResponseBadRequest, HttpResponseServerError, HttpResponse

def generate_username(name):
    return name.lower().replace(" ", "") + ''.join(random.choices(string.digits, k=4))

def upload_student_data(request):
    if request.method == 'POST':
        form = StudentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            filename = uploaded_file.name.lower()

            try:
                # Validate file type
                if filename.endswith('.csv'):
                    df = pd.read_csv(uploaded_file)
                elif filename.endswith(('.xls', '.xlsx')):
                    df = pd.read_excel(uploaded_file)
                else:
                    messages.error(request, "Only .csv, .xls, or .xlsx files are allowed.")
                    return HttpResponseBadRequest(render(request, 'upload.html', {'form': form}))

                # Check required columns
                required_columns = {'name', 'age', 'address', 'email'}
                if not required_columns.issubset(df.columns):
                    messages.error(request, f"File must contain: {', '.join(required_columns)}")
                    return HttpResponseBadRequest(render(request, 'upload.html', {'form': form}))

                # Flag to check if any students were added
                added_any = False

                for index, row in df.iterrows():
                    try:
                        name = row['name']
                        age = int(row['age'])  # might raise ValueError
                        address = row['address']
                        email = row['email']
                        username = generate_username(name)

                        Student.objects.create(
                            name=name,
                            age=age,
                            address=address,
                            email=email,
                            username=username
                        )
                        added_any = True

                    except KeyError as e:
                        messages.warning(request, f"Missing data in row {index + 1}: {e}")
                        continue
                    except ValueError:
                        messages.warning(request, f"Invalid age format in row {index + 1}. Skipped.")
                        continue
                    except Exception as e:
                        messages.warning(request, f"Error in row {index + 1}: {e}")
                        continue

                if added_any:
                    messages.success(request, "Student data uploaded successfully.")
                    return redirect('dashboard')
                else:
                    messages.warning(request, "No valid student records were uploaded.")
                    return render(request, 'upload.html', {'form': form})

            except Exception as e:
                print("Error reading file:", e)
                messages.error(request, f"An internal error occurred: {e}")
                return HttpResponseServerError(render(request, 'upload.html', {'form': form}))

        else:
            return HttpResponseBadRequest(render(request, 'upload.html', {'form': form}))

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