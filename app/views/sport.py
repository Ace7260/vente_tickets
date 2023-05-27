from django.shortcuts import render
from django.http import request
from app.models import Ticket,Category

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
    