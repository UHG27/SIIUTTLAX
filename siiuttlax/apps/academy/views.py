from django.shortcuts import render

from .forms import ProfessorForm, StudentForm

#create your views here.
def create_Professor(request):
    form = ProfessorForm()
    return render(request,
                  'academy/create_professor.html',
                  {'form':form})

def create_student(request):
    form = StudentForm()
    return render(request,'academy/create_student.html',{'form':form})
