from django.urls import path
from .views import home
urlpatterns = [
    path('',home.index,name='home_index' ),
]
