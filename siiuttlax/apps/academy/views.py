from django.shortcuts import redirect, render

from .forms import ProfessorForm, StudentForm

#create your views here.
def create_Professor(request):
    if request.method == 'POST':
        form = ProfessorForm()
    return render(request,
                  'academy/create_professor.html',
                  {'form':form})

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            password = form.cleaned_data['password']
            enrollment = form.cleaned_data['enrollment']

            Student.objects.create_user(
                username=username,
                first_name=password,
                enrollment=enrollment,
                password=password,
            )
            return redirect('academy:create_student')
        
    form = StudentForm()
    return render(request
                  ,'academy/create_student.html',
                  {'form':form})
