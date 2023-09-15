from django.shortcuts import render, redirect
from django.http import request
import jwt, json, os
from dotenv import load_dotenv
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import TemplateView
from app.models import Ticket
from django.contrib.auth.models import User 

load_dotenv()


token_key = os.getenv("TOKEN_KEY")

@login_required(login_url='login_index')
def index(request):
     total_user=User.objects.all().count()
     total_ticket=Ticket.objects.all().count()
     context={
       'total_user':total_user,
       'total_ticket':total_ticket
     }
     return render(
      request,
      'app/home/index.html',context
    )
def come(request):
  return render(
      request,'app/home/comming.html'
    )