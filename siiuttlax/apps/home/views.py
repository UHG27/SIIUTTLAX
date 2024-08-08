from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    user = request.user
    type_user = 'other'
    
    try:
        if user.professor:
            type_user = 'professor'
    except AttributeError:
        pass

    if type_user == 'other':
        try:
            if user.student:
                type_user = 'student'
        except AttributeError:
            pass

    context = {
        "user": user,
        "type_user": type_user
    }

    return render(request, 'home/home.html', context)
