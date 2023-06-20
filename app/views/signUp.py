from django.shortcuts import render,  redirect
from django.http import request
from django.contrib.auth.models import User
from django.contrib import messages
from app.forms import UserForm

def index(request):
  form = UserForm()
  context={
      'form':form
  }
  return render(
    request,
    'app/Auth/signUp.html',context
  )

def save(request):
      if request.method == 'POST':
        form = UserForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            # group = Group.objects.get(name = 'employees')
            # user.groups.add(group)    
            messages.success(request, 'Le compte de '+username+' a été ajouté')
            return redirect('')
        return redirect('/signUp')