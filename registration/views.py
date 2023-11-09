from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from .forms import RegistrationForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Log the user in after registration
            login(request, user)
            
            # can create a "success" URL
            return redirect('success')