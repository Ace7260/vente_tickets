from django.shortcuts import render
from django.http import request
from app.models import Ticket

def index(request):
    return render(
        request,
        'app/tickets/index.html',
    )
    