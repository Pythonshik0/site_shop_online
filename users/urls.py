from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('users-cart/', views.users_cart, name='users_cart'),

]
