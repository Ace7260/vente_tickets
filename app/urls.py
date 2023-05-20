from django.urls import path
from .views import home
urlpatterns = [
    path('',home.index,name='home_index' ),
    # ============== login page =============
    path('login', logout.index, name='login_index'),
    path('login/user', login.loginUser, name="login_user"),
    # ============== signUp page =============
    path('signUp', signUp.index, name='signUp_index'),
    path('signUp/user', signUp.save, name='save_user')
]
