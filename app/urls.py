from django.urls import path
from .views import home, logout,signUp
urlpatterns = [
    path('',home.index,name='home_index' ),
    # ============== login page =============
    path('login', logout.index, name='login_index'),
    # ============== signUp page =============
    path('signUp', signUp.index, name='signUp_index')
]
