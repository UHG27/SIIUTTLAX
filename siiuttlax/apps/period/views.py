# apps/period/views.py
from django.shortcuts import render

def period(request):
    return render(request, 'period/period.html')