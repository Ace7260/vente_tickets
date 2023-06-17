from django.shortcuts import render,  redirect
from django.http import request, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout

def index(request):
  response = HttpResponse(
    render(
      request, 
      'app/Auth/login.html',
    )
  )
  response.delete_cookie('jwt')
  return response
def logout__(request):
	logout(request)
	return redirect('login_index')