# faculty/forms.py

from django import forms
from students.models import StudentProfile
from academics.models import Course

class StudentCourseForm(forms.ModelForm):
    """
    A form for faculty to assign a course to a student.
    """
    course = forms.ModelChoiceField(
        queryset=Course.objects.all().order_by('department__name', 'name'),
        widget=forms.Select(attrs={'class': 'form-select'}),
        help_text="Select the course to assign to the student."
    )

    class Meta:
        model = StudentProfile
        fields = ['course']