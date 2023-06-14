from django.urls import path
from .views import home,category
urlpatterns = [
    path('',home.index,name='home_index' ),
    
    # Category Paths
    path('category/',category.index,name='category_index' ),
    path('category/add/',category.add_index,name='add_category' ),
    path('category/update/<str:pk>',category.update_index,name='update_category'), 
    path('category/delete/<str:pk>',category.delete_index,name='delete_category'),  
]
