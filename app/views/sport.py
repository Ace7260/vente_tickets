from django.shortcuts import render
from django.http import request
from app.models import Ticket

def index(request):
    tickets=Ticket.objects.all()
    return render(
        request,
        'app/sports/index.html',
        {
            'tickets':tickets
        }
    )
    