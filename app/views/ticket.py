from django.shortcuts import render
from django.http import request
from app.models import Ticket
from django.contrib.auth.decorators import login_required

# @login_required(login_url='login_index')
def index(request):
    return render(
        request,
        'app/tickets/index.html',
    )
    