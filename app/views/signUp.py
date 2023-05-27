from django.shortcuts import render,  redirect
from django.http import request
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
  return render(
    request,
    'app/Auth/signUp.html'
  )

def save(request):
    if request.method == 'POST':
        pwd = request.POST.get('password')
        pwd2 = request.POST.get('password2')
        last_name = request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        if(pwd != pwd2):
            messages.error(request,'Password incorrect')
            return redirect('/signUp')
        user = User.objects.create(last_name=last_name, first_name=first_name, username=username, email=email, password=pwd)
        if user :
            return redirect('/login')
        else: 
            messages.error(request,"erreur d'enregistrement")
            return redirect('/signUp')