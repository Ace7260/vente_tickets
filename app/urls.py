from django.urls import path
from app.views import home,sport,ticket,orders,category
urlpatterns = [
    path('',home.index,name='home_index' ),
    # Category Paths
    path('category/',category.index,name='category_index' ),
    path('category/add/',category.add_index,name='add_category' ),
    path('category/update/<str:pk>',category.update_index,name='update_category'), 
    path('category/delete/<str:pk>',category.delete_index,name='delete_category'),  
    # urls for sport
    path('sports',sport.index,name='sport_index'),
    # urls for ticket
    path('tickets',ticket.index,name='ticket_index'),
    # urls for orders
    path('orders',orders.index,name='orders_index'),
   
]
