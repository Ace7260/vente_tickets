from django.shortcuts import render, redirect
from django.http import request
import jwt, json, os
from dotenv import load_dotenv

load_dotenv()


token_key = os.getenv("TOKEN_KEY")


def index(request):
  if "jwt" in request.COOKIES.keys():
    return render(
      request,
      'app/home/index.html'
    )
  else:
    return redirect('/login')