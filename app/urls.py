from app.views import home,sport,ticket
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from django.urls import path
from app.views import home,sport,ticket,orders,category,logout_,login, signUp
urlpatterns = [
    path('',home.index,name='home_index' ),
    # Auth Paths
    # ============== login page =============
    path('login', logout_.index, name='login_index'),
    path('user', login.loginUser, name="login_user"),
    path('logout/', logout_.logout__, name='logout__'),
    
    # ============== signUp page =============
    path('signUp', signUp.index, name='signUp_index'),
    path('signUp/user', signUp.save, name='save_user'),
    
    # Category Paths
    path('category/',category.index,name='category_index' ),
    path('category/add/',category.add_index,name='add_category' ),
    path('category/update/<str:pk>',category.update_index,name='update_category'), 
    path('category/delete/<str:pk>',category.delete_index,name='delete_category'),  

    # urls for sport
    path('sports',sport.index,name='sport_index'),
    path('search/',sport.search,name='search'),
    path("charge/", sport.charge, name="charge"),
    # urls for ticket

    # urls for orders
    path('orders',orders.index,name='orders_index'),
    path('tickets/',ticket.index,name='ticket_index'),
    # urls for home page ticket
    path('tickets/detail/<int:pk>', ticket.detail, name="ticket_detail"),
    # urls to add ticket
    path('tickets/add',ticket.addTicket,name='ticket_add'),
    # urls to update ticket
    path('tickets/edit/<int:pk>', ticket.editTicket, name="ticket_edit"),
    # urls to delete ticket
    path('tickets/delete/<int:pk>', ticket.deleteTicket, name="ticket_delete"),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

