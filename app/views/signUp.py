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
        if(first_name == "" and last_name == "" and email == "" and username == ""):
            messages.error(request, "Please fill in all fields !")
            return redirect('/signUp')
        if(pwd != pwd2):
            messages.error(request,'Passwords incorrect')
            return redirect('/signUp')
        user = User.objects.create(last_name=last_name, first_name=first_name, username=username, email=email, password=pwd)
        if user :
            return redirect('/login')
        else: 
            messages.error(request,"Failed to save")
            return redirect('/signUp')