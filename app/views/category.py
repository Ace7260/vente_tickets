from django.shortcuts import render
from django.http import request

def index(request):
  return render(request,'app/category/index.html')

def add_index(request):
  return render(request,'app/category/add_category.html')