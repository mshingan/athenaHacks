from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import WICSForm
from .models import WICS

# Create your views here.

def home(request):
    ''' home page of wics website '''
    return render(request,'index.html')

def add_client(request):
    ''' accepts form and redirect to home page '''
    if request.method == "POST":
        form = WICSForm(request.POST)
        if form.is_valid():
            wics_item = form.save(commit=False)
            wics_item.save()
            #validate_number(form.phone)
            return redirect('/confirm')
    else:
        form = WICSForm()
    return render(request,'signup.html',{'form': form})

def confirm(request):
    '''confirmation page after signup'''
    return render(request, 'confirmation.html')
