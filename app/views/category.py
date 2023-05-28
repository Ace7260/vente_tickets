from django.shortcuts import render,redirect
from django.http import request
from app.models import *

def index(request):
  categories= Category.objects.all()
  return render(request,'app/category/index.html',{'categories':categories})

def add_index(request):
  
  return render(request,'app/category/add_category.html')