from django.contrib import admin
from django.urls import path
from django.urls import include
from django.contrib.auth import views as auth_views #acceso a las vistas de autenticación 
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),   
    path('', views.index_page, name='index-page'),
    path('login/', auth_views.LoginView.as_view(), name='login'), #Cuando el usuario es redireccionado a login, es autentificado
    path('home/', views.home, name='home'),
    path('buscar/', views.search, name='buscar'),

    path('favourites/', views.getAllFavouritesByUser, name='favoritos'),
    path('favourites/add/', views.saveFavourite, name='agregar-favorito'),
    path('favourites/delete/', views.deleteFavourite, name='borrar-favorito'),

    path('exit/', auth_views.LogoutView.as_view(), name='exit'), #Cuando el usuario es redireccionado a exit, es desauntentificado
]