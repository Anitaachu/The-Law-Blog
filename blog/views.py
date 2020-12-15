from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm
from django.http import HttpResponse

def register(request):  
     if request.method == 'POST':
          form = UserRegisterForm(request.POST)
          if form.is_valid():
               form.save()
               username = form.cleaned_data.get('username')
               messages.success(request, 'Account created for successfully!')
               return redirect('users/login')
     else:
          form = UserRegisterForm()
     return render(request, 'users/register.html/', {'form':form})

