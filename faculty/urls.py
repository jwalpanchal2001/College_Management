# faculty/urls.py

from django.urls import path
from .views import manage_students_view, edit_student_view

urlpatterns = [
    path('students/', manage_students_view, name='faculty_manage_students'),
    path('students/edit/<int:student_id>/', edit_student_view, name='faculty_edit_student'),
]