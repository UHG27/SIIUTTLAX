from django.shortcuts import render

def academy(request):
    return render(request, 'academy/academy.html')