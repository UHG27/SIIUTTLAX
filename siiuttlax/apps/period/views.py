# views.py
from django.shortcuts import render, redirect
from .models import Period
from .forms import PeriodForm

def period_list(request):
    periods = Period.objects.all()
    if request.method == 'POST':
        form = PeriodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('period_list')
    else:
        form = PeriodForm() 
    
    return render(request, 'period/period_list.html', {'periods': periods, 'form': form})
