from django.urls import path
from app.views import home,sport,ticket
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',home.index,name='home_index' ),
    # urls for sport
    path('sports',sport.index,name='sport_index'),
    # urls for ticket
    path('tickets',ticket.index,name='ticket_index'),
    # urls for add ticket
    path('tickets/add', ticket.add, name="ticket_add"),
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
