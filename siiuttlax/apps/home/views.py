from django.shortcuts import redirect, render

# Create your views here.
def home(request):
    user = request.user
    type_user = 'other'
    
    try:
        if user.professor:
            type_user = 'professor'
            return redirect('home:professor')
    except AttributeError:
        pass

    if type_user == 'other':
        try:
            if user.student:
                type_user = 'student'
                return redirect('home:student')
        except AttributeError:
            pass

    context = {
        "user": user,
        "type_user": type_user
    }

    return render(request, 'home/home.html', context)

def student(request):
        user = request.user
        student = user.student
        group = student.group_set.all().first()
        career = group.career

        context= {
            'student': student,
            'group': group,
            'career': career 
        }
        return render(request, 'home/student.html', context)
    
def professor(request):
        user = request.user
        professor = user.professor
        group = professor.group_set.all().first()
        career = group.career 

        context= {
            'student': student,
            'group': group,
            'career': career 
        }
        return render(request, 'home/professor.html', context)