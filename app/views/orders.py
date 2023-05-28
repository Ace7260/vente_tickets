from django.shortcuts import render
from django.http import HttpRequest
from app.models import *

def index(request):
    tickets=Ticket.objects.all()
    return render(request,'app/orders/index.html',{'tickets':tickets})