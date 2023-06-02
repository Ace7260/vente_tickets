from django.shortcuts import render
from django.http import HttpRequest
from app.models import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='login_index')
def index(request):
    tickets=Ticket.objects.all()
    return render(request,'app/orders/index.html',{'tickets':tickets})