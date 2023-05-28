from django.shortcuts import render
from django.http import request,HttpRequest
from app.models import Ticket,Category

def index(request):
    categories=Category.objects.all()
    context={
        'categories':categories
    }
    print(context)
    return render(
        request,
        'app/tickets/add.html',
        context
    )
# Save a new category

from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages

from app.models import Category

# Categories list
def index(request):
    assert isinstance(request, HttpRequest)
    categories = Category.objects.all()
    return render(
        request,
        'app/tickets/add.html',
        {
            'categories': categories
        }
    )

# Add a new category
def add(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        description=request.POST.get('description')
        place=request.POST.get('place')
        price=request.POST.get('price')
        image=request.POST.get('image')
        exp=request.POST.get('exp')
        category=request.POST.get('category')
        tick=Ticket(
            description=description,
            place=place,
            price=price,
            image=image,
            status=True,
            expiration=exp,
            categorie_id=category
        )
        tick.save()
    return render(
        request,
        'app/tickets/add.html'
    )

