from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
import jwt

token_key = "gfggsfg5e54hg5rt4rvwegrh4rg456465e4e56g4rer5g4e56v46e4v5er4gr4v56v1er56g56g56e1cc56156e1g5r1g5e1c51v51rg51r561r5v1e56rg15rt1g56e1v651v56165165b15v1d56b1rb"

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(username, password, user)
         