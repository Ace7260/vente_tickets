from django.shortcuts import render
from django.http import request,HttpResponse
from app.models import Ticket,Category

def index(request):
    tickets=Ticket.objects.all()
    categories=Category.objects.all()
    
    return render(
        request,
        'app/sports/index.html',
        {
            'tickets':tickets,
            'categories':categories
        }
    )
def search(request):
    search_query = request.GET.get('q')
    if search_query:
        # category = search_query
        # categories = Category.objects.filter(description=category)
        # print(categories)
        tickets = Ticket.objects.filter(categorie__description=search_query)
        print(tickets,'======')
        return render(request, 'app/sports/index.html', { 'tickets': tickets})
    else:
        categories = Category.objects.all()
        tickets = Ticket.objects.all()
        return render(request, 'app/sports/index.html', {'categories': categories, 'tickets': tickets})