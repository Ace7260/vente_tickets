from django.urls import path
from app.views import home,sport,ticket,orders
urlpatterns = [
    path('',home.index,name='home_index' ),
    # urls for sport
    path('sports',sport.index,name='sport_index'),
    # urls for ticket
    path('tickets',ticket.index,name='ticket_index'),
  
    path('orders',orders.index,name='orders_index'),
    
    
]
