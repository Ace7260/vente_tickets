from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
import jwt

token_key = "JJhjhjhiidigdigigJHUGUGUHIjiIJhijhjihdjighjidhjsshjdf4df56b456dsdnvjbddjdb1d651b5dbvnjshgHVHHjidgd4df54dnhjBHBhjbjkndkn"



def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            print("USER_DATA : ",user)
            # user_data = User.objects.get(username=username)
            login(request, user)
            token = jwt.encode({'username': username}, token_key, algorithm='HS256')
            response = HttpResponse(
                render(
                    request, 
                    'app/home/index.html'
                )
            )
            response.set_cookie('jwt', token)
            print("TOKEN : ", token)
            return response
        else:
            print("Error de connexion")
            messages.error(request, 'Les informations fournies ne sont pas correctes.')
            return redirect('/login') 