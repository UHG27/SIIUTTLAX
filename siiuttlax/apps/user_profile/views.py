from django.shortcuts import render
from django.contib.auth.decorators import login_requirer


# Create your views here.
@login_required
def home( request):
    user = request.user
    try:
        if user.prodessor:
            type_user = 'professor'
        if user.student:
            type_user = 'student'
    except:
        type_user = 'other'
    context = {
    "user": user,   def get_queryset(self):
        return super().get_queryset()
    
        "type_user": type_user
    }
