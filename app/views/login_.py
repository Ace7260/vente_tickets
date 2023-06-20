from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from datetime import datetime, timedelta
import jwt, json, os
from django.contrib.auth import authenticate,login
from dotenv import load_dotenv

load_dotenv()


token_key = os.getenv("TOKEN_KEY")


def loginUser(request):
  if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(request.POST)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            messages.info(request, 'Nom d\'utilisateur ou mot de passe incorrect')

        template  = 'app/Auth/login.html'
    
 

        return render(request,
        template_name = template    )