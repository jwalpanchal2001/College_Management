# faculty/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from accounts.decorators import faculty_required
from accounts.models import CustomUser
from students.models import StudentProfile
from .forms import StudentCourseForm
from django.db.models import Q

@faculty_required
def manage_students_view(request):
    """
    Displays a filterable and sortable list of all students for faculty.
    """
    query = request.GET.get('q')
    sort_by = request.GET.get('sort', 'username')

    students = CustomUser.objects.filter(user_type=3)

    if query:
        students = students.filter(
            Q(username__icontains=query) | Q(email__icontains=query)
        )

    # Apply sorting
    if sort_by == 'username_desc':
        students = students.order_by('-username')
    elif sort_by == 'date_joined':
        students = students.order_by('date_joined')
    elif sort_by == 'date_joined_desc':
        students = students.order_by('-date_joined')
    else:
        students = students.order_by('username')
        
    context = {
        'students': students,
        'query': query,
        'current_sort': sort_by,
    }
    return render(request, 'faculty/manage_students.html', context)

@faculty_required
def edit_student_view(request, student_id):
    """
    Handles the form for a faculty member to edit a student's course.
    """
    student_profile = get_object_or_404(StudentProfile, user_id=student_id)
    
    if request.method == 'POST':
        form = StudentCourseForm(request.POST, instance=student_profile)
        if form.is_valid():
            form.save()
            messages.success(request, f"Successfully updated course for {student_profile.user.username}.")
            return redirect('faculty_manage_students')
    else:
        form = StudentCourseForm(instance=student_profile)

    context = {
        'form': form,
        'student_profile': student_profile
    }
    return render(request, 'faculty/edit_student.html', context)