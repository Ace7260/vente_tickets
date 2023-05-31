from django.shortcuts import render
from django.http import request
from app.models import Ticket,Category
from django.contrib.auth.decorators import login_required

@login_required(login_url='login_index')
def index(request):
    tickets=Ticket.objects.all()
    categories=Category.objects.all()
    
    return render(
        request,
        'app/sports/index.html',
        {
            'tickets':tickets,
            'categories':categories
        }
    )
    