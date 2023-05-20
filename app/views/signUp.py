from django.shortcuts import render,  redirect
from django.http import request
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
  return render(
    request,
    'app/Auth/signUp.html'
  )

