from django.shortcuts import render
from django.http import request
from django.shortcuts import render
from django.views.generic import TemplateView
from app.models import User

def index(request):
  return render(
    request,
    'app/home/index.html'
  )

def count_users(request):
    total_users = User.objects.count()
    return render(request, "app/home/index.html", {"total_users": total_users})