from django.urls import path
from .views import home,category
urlpatterns = [
    path('',home.index,name='home_index' ),
    path('category/',category.index,name='category_index' ),
]
