from django.shortcuts import render,redirect
from django.http import request
from app.models.category import Category
from app.forms.categoryForm import CategoryForm
from django.contrib.auth.decorators import login_required

# @login_required(login_url='login_index')
def index(request):
  categories= Category.objects.all()
  return render(request,'app/category/index.html',{'categories':categories})
# @login_required(login_url='login_index')
def add_index(request):
  form=CategoryForm()
  if request.method == 'POST':
    form=CategoryForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/category/')
  context={'form':form} 
  return render(request,'app/category/add_category.html',context)

# @login_required(login_url='login_index')
def update_index(request,pk):
  
  category =Category.objects.get(id=pk)
  form=CategoryForm(instance=category)
  if request.method == 'POST':
    form=CategoryForm(request.POST,instance=category)
    if form.is_valid():
      form.save()
      return redirect('/category/')
    
  context={'form':form}
  return render(request,'app/category/add_category.html',context)
# @login_required(login_url='login_index')
def delete_index(request,pk):
  category =Category.objects.get(id=pk)
  context={'category':category}
  category.delete()
  redirect('/category/')
  return render(request,'app/category/index.html')