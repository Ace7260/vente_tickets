from django.shortcuts import render,  redirect
from django.http import request
from app.forms import signUp_form
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
        if(pwd != pwd2):
            messages.error(request,'Password incorrect')
        form = signUp_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Enregistrement avec success')
            return redirect('/login')