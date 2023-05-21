from django.urls import path
from app.views import home,sport
urlpatterns = [
    path('',home.index,name='home_index' ),
    # urls for sport
    path('sports',sport.index,name='sport_index'),
]
