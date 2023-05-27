from django.shortcuts import render
from app.models import *
from app.utile import  data_cookie
def panier(request, *args, **kwargs):
    data = data_cookie(request)
    articles = data['articles']
    commande = data['commande']
    nombre_article = data['nombre_article']
    context = {
        'articles':articles,
        'commande':commande,
        'nombre_article':nombre_article
    }

    return render(request, 'app/sports/panier.html', context)
