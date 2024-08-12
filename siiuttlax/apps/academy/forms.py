from .models import Professor, Student
from django import forms

class ProfessorForm(forms.ModelForm):

    class Meta:
        model = Professor
        fields = ['username', 'password', 'first_name', 'employee_number']
        widgets = {
            'password': forms.PasswordInput(),
            'employee_number': forms.NumberInput(),
        }

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['username', 'password', 'first_name', 'enrollment']
        widgets = {
            'password': forms.PasswordInput()
        }
