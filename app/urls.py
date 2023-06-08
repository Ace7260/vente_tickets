from django.urls import path
from app.views import home,sport,ticket
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',home.index,name='home_index'),
    # urls for sport
    path('sports',sport.index,name='sport_index'),
    # urls for ticket
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

