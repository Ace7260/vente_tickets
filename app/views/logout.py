from django.shortcuts import render,  redirect
from django.http import request, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
  response = HttpResponse(
    render(
      request, 
      'app/Auth/login.html',
    )
  )
  response.delete_cookie('jwt')
  return response
def logout(request):
	logout(request)
	return redirect('login_index')