from django.urls import path
from .views import upload_student_data, student_dashboard, delete_student, edit_student

urlpatterns = [
    path('upload/', upload_student_data, name='upload_student_data'),
    path('dashboard/', student_dashboard, name='dashboard'),
    path('delete/<int:id>/', delete_student, name='delete_student'),
    path('edit/<int:id>/', edit_student, name='edit_student'),
]