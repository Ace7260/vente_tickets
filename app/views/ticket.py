from django.shortcuts import render
from django.http import request


def index(request):
    return render(
        request,
        'app/ticket/index.html'
    )
    